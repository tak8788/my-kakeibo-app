from urllib.parse import quote
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="資産管理ダッシュボード", layout="wide")
st.title("資産管理 & 家計ダッシュボード")


# 1. スプレッドシートからのデータ読み込み
@st.cache_data(ttl=600)
def load_data():
    sheet_id = "1cG-Oa2sYQJlaD3MV1kf6YK-BuF-ayTPki2NvyQiay7c"

    # 日本語シート名をURLエンコード化
    sheet_asset = quote("資産")
    sheet_expense = quote("月別費用")

    asset_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_asset}"
    expense_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_expense}"

    df_asset = pd.read_csv(asset_url)
    df_expense = pd.read_csv(expense_url)

    # 列名の前後にある余計な空白を削除
    df_asset.columns = df_asset.columns.str.strip()
    df_expense.columns = df_expense.columns.str.strip()

    # 資産データの数値クリーニング
    for col in df_asset.columns:
        if col != "年月":
            df_asset[col] = (
                df_asset[col]
                .astype(str)
                .str.replace(",", "")
                .str.replace("←.*", "", regex=True)
            )
            df_asset[col] = pd.to_numeric(df_asset[col], errors="coerce").fillna(0)

    # 支出データの数値クリーニング
    for col in df_expense.columns:
        if col != "年月":
            df_expense[col] = (
                df_expense[col]
                .astype(str)
                .str.replace(",", "")
                .str.replace("¥", "")
                .str.replace("←.*", "", regex=True)
            )
            df_expense[col] = pd.to_numeric(
                df_expense[col], errors="coerce"
            ).fillna(0)

    return df_asset, df_expense


df_asset, df_expense = load_data()

# --- タブ表示 ---
tab1, tab2 = st.tabs(["資産推移", "支出分析"])

# === タブ1: 資産推移 ===
with tab1:
    st.header("資産推移")
    latest_asset = df_asset.dropna(subset=["年月"]).iloc[-1]

    # 合計列の安全な取得
    total_asset = latest_asset.get("合計", 0)
    st.metric(
        label=f"最新総資産 ({latest_asset['年月']})",
        value=f"{int(total_asset):,} 円",
    )

    asset_cols = [
        c
        for c in df_asset.columns
        if c not in ["年月", "合計"] and not c.startswith("Unnamed")
    ]
    fig_asset = px.bar(
        df_asset,
        x="年月",
        y=asset_cols,
        title="資産内訳の推移",
        barmode="stack",
    )
    st.plotly_chart(fig_asset, use_container_width=True)


# === タブ2: 支出分析 ===
with tab2:
    st.header("月別費用の分析")

    # 最新月のサマリー表示
    latest_exp = df_expense.dropna(subset=["年月"]).iloc[-1]
    col1, col2 = st.columns(2)

    total_exp = latest_exp.get("合計", 0)
    with col1:
        st.metric(
            label=f"最新月の支出合計 ({latest_exp['年月']})",
            value=f"{int(total_exp):,} 円",
        )
    with col2:
        if "住宅ローン" in latest_exp:
            st.metric(
                label="住宅ローン", value=f"{int(latest_exp['住宅ローン']):,} 円"
            )

    # 分析対象とする費目のリスト（実データに存在する列のみ動的抽出）
    candidate_cols = [
        "家賃",
        "食費",
        "生活日用品",
        "通信費",
        "趣味・娯楽",
        "水道光熱費",
        "交際費",
        "保険料",
        "衣服・美容",
    ]
    expense_cols = [c for c in candidate_cols if c in df_expense.columns]

    # 1. 月別支出内訳の積み上げ棒グラフ
    if expense_cols:
        fig_exp_bar = px.bar(
            df_expense,
            x="年月",
            y=expense_cols,
            title="月別支出内訳の推移",
            barmode="stack",
        )
        st.plotly_chart(fig_exp_bar, use_container_width=True)

        # 2. 最新月の支出割合（円グラフ）
        latest_data = latest_exp[expense_cols].reset_index()
        latest_data.columns = ["費目", "金額"]
        latest_data = latest_data[latest_data["金額"] > 0]

        if not latest_data.empty:
            fig_pie = px.pie(
                latest_data,
                values="金額",
                names="費目",
                title=f"最新月 ({latest_exp['年月']}) の支出内訳割合",
                hole=0.4,
            )
            st.plotly_chart(fig_pie, use_container_width=True)

    # 3. 元データ一覧
    with st.expander("月別費用データ一覧を見る"):
        st.dataframe(df_expense)
