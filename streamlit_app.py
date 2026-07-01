from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="세컨부스트 — 독자별 산출물 대시보드",
    page_icon="🗂️",
    layout="wide",
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=2600, scrolling=True)
