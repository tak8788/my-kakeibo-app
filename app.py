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

    # 数値列のクリーニング
    for col in df_asset.columns:
        if col != "年月":
            df_asset[col] = (
                df_asset[col]
                .astype(str)
                .str.replace(",", "")
                .str.replace("←.*", "", regex=True)
            )
            df_asset[col] = pd.to_numeric(df_asset[col], errors="coerce").fillna(0)

    return df_asset, df_expense


df_asset, df_expense = load_data()

# --- タブ表示 ---
tab1, tab2 = st.tabs(["資産推移", "支出分析"])

with tab1:
    st.header("資産推移")
    latest = df_asset.dropna(subset=["年月"]).iloc[-1]
    st.metric(
        label=f"最新総資産 ({latest['年月']})",
        value=f"{int(latest['合計']):,} 円",
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

with tab2:
    st.header("月別費用")
    st.dataframe(df_expense)
