import streamlit as st

st.title("Media - image")

# 서버 이미지
st.image("../data/image1.gif", caption="아아 그랬구나")

# 웹 이미지
image_url = "https://mblogthumb-phinf.pstatic.net/20160510_39/zooiddqd_14628883516235Srnc_JPEG/0120edaab213355330e4e7c514afe7853c7b982e06.jpg?type=w420"
st.image(image_url, caption="웹 이미지")