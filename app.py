import streamlit as st
import random

def main():
    # アプリのタイトル
    st.title("ランダムな数字")

    # 数字の範囲を指定するスライダー
    st.sidebar.title("範囲を指定してください")
    min_value = st.sidebar.number_input("最小値", value=10, step=1)
    max_value = st.sidebar.number_input("最大値", value=99, step=1)

    if min_value >= max_value:
        st.sidebar.error("最小値は最大値より小さくしてください！")
        return

    # セッション状態を使用してランダムな数字を保持
    if "random_number" not in st.session_state:
        st.session_state.random_number = None

    # 2桁の数字を生成ボタン
    if st.button("2桁の数字を生成"):
        st.session_state.random_number = random.randint(min_value, max_value)

    # 現在のランダムな数字を表示
    if st.session_state.random_number is not None:
        st.markdown(f"<p style='font-size: 5em;'>{st.session_state.random_number}</p>", unsafe_allow_html=True)

    # 答えを表示するボタン
    if st.session_state.random_number is not None and st.button("2乗数を表示"):
        square = st.session_state.random_number ** 2
        st.markdown(f"<p style='font-size: 5em;'> {square}</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
