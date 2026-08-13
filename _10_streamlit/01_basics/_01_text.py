import streamlit as st

# 실행 명령어
# streamlit run [파일명].py

# 페이지 제목
st.title("🫠Hello, Streamlit!😊")

st.header("Text", divider="rainbow")
st.subheader(":green[sub]header", divider="red")

# text : 단순 글자
st.text("text 테스트!!!")

# write
# - 단순 글자 뿐만 아니라
#  마크다운, 표, 리스트, 차트,
#  입력 타입 등에 따라 출력방식 정해짐
st.write("write 테스트!!!")
st.write("write **markdown** 지원")
st.write("`write`")
st.markdown("### markdown")
st.html("<h3><mark>html</mark>도 지원</h3>")


st.subheader(":red[magic]", divider="orange")

"streamlit magic"
"변수나 리터럴 값이 출력 구문내에 없어도 화면에 값을 기록하는 기능"
100

lst = [10, 20, 30]
lst

dct = {"a": 10, "b": 20}
dct


# 코드 블록
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language="python", line_numbers=True)

# latex : 수식
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

# 뱃지
st.badge("New")
st.badge("Success", icon=":material/check:", color="green")

st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# metric : 측량, 측정
st.subheader(":blue[metric]", divider="blue")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# columns() 컬럼 분할
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


from numpy.random import default_rng as rng

changes = list(rng(4).standard_normal(20))
data = [sum(changes[:i]) for i in range(20)]
delta = round(data[-1], 2)

row = st.container(horizontal=True)
with row:
    st.metric(
        "Line", 10, delta, chart_data=data, chart_type="line", border=True
    )
    st.metric(
        "Area", 10, delta, chart_data=data, chart_type="area", border=True
    )
    st.metric(
        "Bar", 10, delta, chart_data=data, chart_type="bar", border=True
    )