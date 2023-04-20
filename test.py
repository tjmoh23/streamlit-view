# Terminal에 streamlit hello 입력하여 streamlit 실행
# streamlit run test.py - 웹 페이지에 출력하기
import streamlit as st

view = [100, 150, 30]
st.write("# Youtube view")
st.write("## raw")
view
st.write("## bar chart")
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview

st.write("### Streamlit에 대해 배워보자!")
