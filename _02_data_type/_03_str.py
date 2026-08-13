

# str (문자형, 문자열, String)
# "", '', """ """, ''' ''' 감싸서 표현

print("--- 홑 따옴표, 쌍 따옴표 ---")
s1 = 'Hello'
s2 = "World"

s3 = "'abc'"

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# 삼중 따옴표
print(""" 
삼중 따옴표는
입력된 형식 그대로 문자열(str)로 변환
""")

print("""앞/뒤 엔터 없이 작성하려면
따옴표와 문자열을 딱 붙여서 작성""")


# str 연산

# 1. 문자열 + 문자열 = 이어쓰기
print('--- 문자열 더하기 연산 ---')
a = 'apple'
b = 'banana'
print(a + ', ' + b) # apple, banana

# 2. 문자열 * 양의 정수 = 양의 정수 크기 만큼 반복
print('-' * 30)
print('❤️' * 30)

# 빼기, 나누기 연산을 불가
# print('a' - 'b');
# TypeError: unsupported operand type(s) for -: 'str' and 'str'



# len(객체) 함수: 파이썬 객체 길이 반환
# 파이썬 객체: str, list, tuple, dict, set 등
print('--- len() ---')
text = '오늘 점심은 뭘먹죠?'
print(text, len(text))

# --- str 메서드 (str api) ---
# (참고) 함수, 메서드 == 기능(실행 후 결과 반환)

# str.replace(old, new)
# - str 내에서 old에 해당하는 문자를 new로 치환(변경)
print('--- str.replace() ---')
today = '2026-06-01'
print(today, today.replace('-', '/'))

# str.strip([str])
# - 문자열 좌우 [str] 제거
# - [str] 생략 시 공백 제거
# - 코드 작성법에서 []는 생략 가능을 뜻함
print('--- str.strip() ---')
some = '          하하하           '
print('[' + some + ']')
print('[' + some.strip() + ']')

# 대소문자 관련 str 메서드
print('--- 대소문자 관련 str 메서드 ---')
origin_str = 'hELLO wORLD!'
print(origin_str.upper())         # HELLO WORLD!
print(origin_str.lower())         # hello world!
print(origin_str.capitalize())    # Hello world!
print(origin_str.swapcase())      # Hello World!
print(origin_str.title())         # Hello World!


# 문자열 포맷팅

# 1. % 포맷팅
print('--- % 포맷팅 ---')
x = 10
print("x is %d" %x)    # x is 10

# 2. str.format()
print('--- str.format() ---')
x = 10
y = 1.23
print('{} + {} = {}'.format(x, y, x + y))

# 3. f-string (python 3.6)
print("--- f-string ---")
print(f"{x} + {y} = {x+y}")

# ---------------------------------------
# 문자열 인덱싱/슬라이싱
# - 파이썬 문자열(str)은 text sequence 형태를 갖는다
# - sequence: 순차적인, 순서가 있는 데이터 구조
# - index: 순서 (base index == 0)
# - 마지막 index == str길이 -1

print("--- 문자열 indexing ---")
x = 'Monday'
print('x의 길이: ', len(x)) # 길이 6, 인덱스 0,1,2,3,4,5
print(x[0]) # [] == 배열, [0] == str 배열 중 0번째 index
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])
# print(x[6]) # 초과, IndexError: string index out of range

# 역 인덱스: str을 거꾸로 탐색
print(x[-1], x[-2], x[-3], x[-4], x[-5], x[-6])

# str 슬라이싱: 문자열 일부를 잘라서 가져오는 방법
# 작성법:   str[start:stop:step]
# - start: 시작 인덱스
# - stop: 종료 인덱스 (미포함)
# - step: 건너 뛸 개수 (생략 시 기본 값 1)
print("--- str slicing ---")

text = 'hello world'
print("text: ", text)
print("len(text): ", len(text))

print("text[0:5:1]: ", text[0:5:1])
print("text[0:5]: ", text[0:5])
print("text[:5]: ", text[:5])

print("text[6:11]: ", text[6:11])
print("text[6:len(text)]: ", text[6:len(text)])
print("text[6:]: ", text[6:]) # 6 시작, 끝까지
print("text[:]: ", text[:]) # 0 ~ 끝까지

print("text[0:11:2]: ", text[0:11:2]) # 0, 2, 4, 8, 10
print("text[::2]: ", text[::2]) # 0, 2, 4, 8, 10
print("text[::-1]: ", text[::-1]) # 문자열 뒤집기


# 문자열 불변 타입(immutable)
# - str은 한 번 메모리에 값이 저장되면 수정할 수 없다.

# id(변수명): 변수에 저장된 값의 주소(위치)를 반환
print("--- 문자열 불변 타입 ---")
s = 'python'   # s에는 'python' str 메모리 주소가 저장됨
print("s: ", s)  # s에 저장된 주소를 찾아가서 'python' str을 참조
print("변경 전 s: ", id(s))

s = s + ' hello'
print("s: ", s)
print("변경 후 s: ", id(s))


# in 연산자(멤버쉽 검사 연산자)
# - 특정 값이 포함되어 있는지 검사
# - 결과는 bool 형태
print("--- in 연산자 ---")
txt = "김밥, 라면, 어묵, 떡볶이"
print('라면' in txt) # True
print('돈까스' in txt) # False


