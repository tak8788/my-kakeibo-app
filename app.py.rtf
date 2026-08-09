{\rtf1\ansi\ansicpg932\cocoartf2865
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import pandas as pd\
import plotly.express as px\
import streamlit as st\
\
st.set_page_config(page_title="\uc0\u36039 \u29987 \u31649 \u29702 \u12480 \u12483 \u12471 \u12517 \u12508 \u12540 \u12489 ", layout="wide")\
st.title("\uc0\u36039 \u29987 \u31649 \u29702  & \u23478 \u35336 \u12480 \u12483 \u12471 \u12517 \u12508 \u12540 \u12489 ")\
\
\
# 1. \uc0\u12473 \u12503 \u12524 \u12483 \u12489 \u12471 \u12540 \u12488 \u12363 \u12425 \u12398 \u12487 \u12540 \u12479 \u35501 \u12415 \u36796 \u12415 \u65288 Web\u20844 \u38283 URL\u12363 \u12425 CSV\u24418 \u24335 \u12391 \u21462 \u24471 \u65289 \
@st.cache_data(ttl=600)  # 10\uc0\u20998 \u12461 \u12515 \u12483 \u12471 \u12517 \
def load_data():\
    sheet_id = "1cG-Oa2sYQJlaD3MV1kf6YK-BuF-ayTPki2NvyQiay7c"\
\
    # \uc0\u36039 \u29987 \u12471 \u12540 \u12488 \u65288 gid=0 \u12414 \u12383 \u12399 \u12471 \u12540 \u12488 \u21517 \u25351 \u23450 \u65289 \
    asset_url = f"https://docs.google.com/spreadsheets/d/\{sheet_id\}/gviz/tq?tqx=out:csv&sheet=\uc0\u36039 \u29987 "\
    # \uc0\u26376 \u21029 \u36027 \u29992 \u12471 \u12540 \u12488 \
    expense_url = f"https://docs.google.com/spreadsheets/d/\{sheet_id\}/gviz/tq?tqx=out:csv&sheet=\uc0\u26376 \u21029 \u36027 \u29992 "\
\
    df_asset = pd.read_csv(asset_url)\
    df_expense = pd.read_csv(expense_url)\
\
    # \uc0\u12463 \u12522 \u12540 \u12491 \u12531 \u12464 \u65288 \u12459 \u12531 \u12510 \u38500 \u21435 \u12392 \u25968 \u20516 \u21270 \u65289 \
    for col in df_asset.columns:\
        if col != "\uc0\u24180 \u26376 ":\
            df_asset[col] = (\
                df_asset[col]\
                .astype(str)\
                .str.replace(",", "")\
                .str.replace("\uc0\u8592 .*", "", regex=True)\
            )\
            df_asset[col] = pd.to_numeric(df_asset[col], errors="coerce").fillna(0)\
\
    return df_asset, df_expense\
\
\
df_asset, df_expense = load_data()\
\
# --- \uc0\u12479 \u12502 \u34920 \u31034  ---\
tab1, tab2 = st.tabs(["\uc0\u36039 \u29987 \u25512 \u31227 ", "\u25903 \u20986 \u20998 \u26512 "])\
\
with tab1:\
    st.header("\uc0\u36039 \u29987 \u25512 \u31227 ")\
    # \uc0\u30452 \u36817 \u12398 \u36039 \u29987 \u32207 \u38989 \
    latest = df_asset.dropna(subset=["\uc0\u24180 \u26376 "]).iloc[-1]\
    st.metric(\
        label=f"\uc0\u26368 \u26032 \u32207 \u36039 \u29987  (\{latest['\u24180 \u26376 ']\})",\
        value=f"\{int(latest['\uc0\u21512 \u35336 ']):,\} \u20870 ",\
    )\
\
    # \uc0\u20869 \u35379 \u12464 \u12521 \u12501 \u65288 \u12501 \u12467 \u12463 \u12289 PayPay\u37504 \u34892 \u12289 \u27005 \u22825 \u37504 \u34892 \u12289 \u27005 \u22825 \u35388 \u21048 \u12289 \u19977 \u20117 \u20303 \u21451 \u12394 \u12393 \u65289 \
    asset_cols = [\
        c\
        for c in df_asset.columns\
        if c not in ["\uc0\u24180 \u26376 ", "\u21512 \u35336 "] and not c.startswith("Unnamed")\
    ]\
    fig_asset = px.bar(\
        df_asset,\
        x="\uc0\u24180 \u26376 ",\
        y=asset_cols,\
        title="\uc0\u36039 \u29987 \u20869 \u35379 \u12398 \u25512 \u31227 ",\
        barmode="stack",\
    )\
    st.plotly_chart(fig_asset, use_container_width=True)\
\
with tab2:\
    st.header("\uc0\u26376 \u21029 \u36027 \u29992 ")\
    st.dataframe(df_expense)}