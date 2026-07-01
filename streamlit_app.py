from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="세컨부스트 — 독자별 산출물 대시보드",
    page_icon="🗂️",
    layout="wide",
)

# Streamlit이 기본으로 씌우는 여백·헤더·푸터를 제거하고, 임베드된 iframe이
# 브라우저 뷰포트 전체를 채우도록 강제한다. 이렇게 해야 대시보드 내부의
# position:sticky 탭바가 (이중 스크롤 없이) 실제로 화면 상단에 고정된다.
st.markdown(
    """
    <style>
      #MainMenu, header[data-testid="stHeader"], footer { display: none !important; }
      .block-container { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
      div[data-testid="stAppViewContainer"] { padding: 0 !important; }
      iframe { height: 100vh !important; width: 100% !important; border: none !important; display: block; }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1000, scrolling=True)
