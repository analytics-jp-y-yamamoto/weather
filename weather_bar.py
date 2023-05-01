import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# ページのタイトル設定
st.set_page_config(
    page_title = "bar",
)

# csv読み込み
df0 = pd.read_csv('/Users/yamamotoyuta/Downloads/data.csv', index_col = 0)

# セッション情報の初期化
if "page_id" not in st.session_state:
    st.session_state.page_id = -1
    st.session_state.df0 = df0

# 各種メニューの非表示設定
hide_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_style, unsafe_allow_html = True)

# 最初のページ
def main_page():
    st.markdown(
        "<h2 style='text-align: center;'>棒グラフ表示</h2>",
        unsafe_allow_html = True,
    )

    day_list = st.session_state.df0.index.values
    column_list = st.session_state.df0.columns.values
    day_list_selector = st.sidebar.selectbox("日時選択", day_list)
    column_list_selector = st.sidebar.selectbox("表示内容選択", column_list)

    top5=st.session_state.df0.sort_values(column_list_selector, ascending = False)[column_list_selector][:5]

    fig1, ax1 = plt.subplots(figsize = (6.4, 4.8))

    ax1.bar(st.session_state.df0.index.values,st.session_state.df0[column_list_selector])
    ax1.set_title("横浜"+column_list_selector)
    ax1.set_xlabel("日時")
    ax1.set_ylabel("気温")

    fig2, ax2 = plt.subplots(figsize = (9.0, 5.4))

    ax2.bar(top5.index.values, top5)
    ax2.set_title("横浜"+column_list_selector+"TOP5")
    ax2.set_xlabel("日時")
    ax2.set_ylabel("気温")

    st.pyplot(fig1)
    st.pyplot(fig2)
    st.text(st.session_state.df0[column_list_selector])
# ページ判定
if st.session_state.page_id == -1:
    main_page()
