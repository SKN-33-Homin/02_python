import streamlit as st

st.title("😇 Input Widgets 😇")
st.header("Button", divider="rainbow")

# button 생성 + 입력 값 저장
clicked = st.button("Click Me")
print("clicked: ", clicked) # 파이썬 콘솔에 출력

if clicked:
    st.write("버튼이 클릭 되었습니다!!")
else:
    st.write("아직 버튼을 클릭하지 않았습니다.")

st.button("리셋버튼입니다~")



st.subheader("Text Input", divider="rainbow")

destination = st.text_input(
    label="가고 싶은 여행지가 있으신가요?",
    placeholder="여행지를 입력하세요"
)
st.write("입력된 여행지: ", destination)


txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.")

# 라디오 버튼 (여러 개 중 한 가지만 선택)
st.subheader("Radio Buttons", divider="rainbow")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ],
)

if genre == ":rainbow[Comedy]":
    st.write("You selected comedy.")
else:
    st.write("You didn't select comedy.")



st.header('SelectBox')
# 선택 박스
mbti = st.selectbox(
    '당신의 MBTI는 무엇입니까?',
    ('ISTJ', 'ISFJ', 'INFJ', 'INTJ',
     'ISTP', 'ISFP', 'INFP', 'INTP',
     'ESTP', 'ESFP', 'ENFP', 'ENTP',
     'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ',
     '모름'),
    index=7
)
if mbti:
    st.write(f'선택한 MBTI는 :red[{mbti}]입니다.')



agree = st.checkbox("I agree")

if agree:
    st.write("Great!")