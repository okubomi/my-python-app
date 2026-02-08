# app.py
import streamlit as st

# ページのタイトル
st.set_page_config(page_title="My First App")
st.title("🚀 はじめてのStreamlit公開アプリ")

# ユーザー入力を受け取る
name = st.text_input("あなたのお名前を教えてください", "ゲスト")

# ボタンを押した時の処理
if st.button("挨拶を表示"):
    st.balloons()  # お祝いの風船を飛ばす
    st.success(f"こんにちは、{name}さん！このアプリはWeb上で動いています。")

st.write("---")
st.caption("作成者: [あなたの名前] / ポートフォリオ第1号")
