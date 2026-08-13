import streamlit as st

st.title('session station')

description = """
- Streamlit : 버튼 클릭 등 사용자 상호 작용이 발생 시 새로 읽음,
              일반 변수에 저장 된 변수 매번 초기화

- Session State : 같은 사용자 내에서 값을 유지
                  (사용자 기준 == Browser)
"""

st.markdown(description)

count: int = 0 # Button Click 횟수 세기, 초기값 0

# clicked = st.button("클릭시 횟수 1 증가")
#
# clicked #Magic

if st.button("클릭시 횟수 1 증가"):
    count += 1

st.write("클릭 횟수 :",count)

st.subheader('Session State를 이용한 카운트', divider=True)

cnt : int = 0
# session stat : 서버 컴퓨터 메모리 영역에 접속한 사용자 별 객체
if 'cnt' not in st.session_state: #cnt가 session 내부에 없으면
    st.session_state['cnt'] = 0 # 초기화, 최초 1회만 실행

if st.button("클릭시 횟수 1회 증가"): #session state에 저장된 값 제외 초기화됨
    st.session_state['cnt'] += 1

if st.button("클릭시 횟수 1회 증감"): #session state에 저장된 값 제외 초기화됨
    st.session_state['cnt'] -= 1

if st.button("클릭시 횟수 초기화"): #session state에 저장된 값 제외 초기화됨
    st.session_state['cnt'] = 0

st.write("클릭 횟수 :",st.session_state['cnt'])