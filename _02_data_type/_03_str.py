# str (문자열, 문자형, String)
# ', ", """, ''' 등으로 감싸서 표현

print("--- 홑따옴표, 쌍따옴표 ---")
s1 = 'Hello'
s2 = "World"
s3 = "'abc'"
print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))

# 삼중 따옴표

print("""삼중 따옴표는 
입련된
형식 그대로
문자열(str)로 변환
""")

print("""앞/뒤 공백 없이 작성하려면 딱 붙여서 작성""")

# str의 연산

# 1. 문자열 + 문자열 = 분자 이어 쓰기
print("---문자열 + 문자열---")

a = "apple"
b = "banana"

print(a + ', '+ b)

# 2. 문자열 * 양의 정수 = 양의 정수 만큼 문자열 반복

print("-" * 30)
print("---문자열 * 양의 정수---")

#len(객체) 함수 : 파이썬 객체 길이 반환
# 파이썬 객체 : str, list, tuple, dict, set  등
print("--- len() ---")
a = "오늘 점심 뭐 먹죠"
print(a, len(a))

# str 매서드 (str api)
# (참고) 함수, 매서드 모두 기능을 뜻하며 결과 값이 나옴

# str.replace(old, new)
# str 내에서 old에 해당하는 문자를 new로 치환
print("--- str.replace() ---")
today = "2026-06-01"
print(today, today.replace("-" , '/'))

# str.strip([str]) : 문자열 좌우 [str]제거
# [] 생략시 공백 제거
# 코드 작성법에서 []는 생략 가능

print('--- str.strip() ---')

some = '          하하하           '
print('[' + some+ ']')
print('[' + some.strip()+ ']')

# 대소문자 관련 str 매서드

"""
1. upper() : 대문자로 변경한다.
2. lower() : 소문자로 변경한다.
3. capitalize() : 첫 글자만 대문자로 변경한다.
4. swapcase() : 대문자는 소문자로, 소문자는 대문자로 변경한다.
5. title() : 단어의 첫글자를 대문자로 변경한다.
"""

print("---대소문자 관련 str 매서드---")
origin_str = 'hELLO wORLD!'

print(origin_str.upper())         # HELLO WORLD!
print(origin_str.lower())         # hello world!
print(origin_str.capitalize())    # Hello world!
print(origin_str.swapcase())      # Hello World!
print(origin_str.title())         # Hello World!

# 문자열 포맷팅

"""
- 변수 포맷 종류
    - %s : 문자열
    - %c : 문자
    - %d : 정수
    - %f : 실
"""

x = 10
print("x is %d" %x)    # x is 10

y = "code"
print("y is %s" %y)    # y is code

x, y = 10, "code"
print("x is {0}".format(x))                                        # x is 10
print("x is {0} y is {1}".format(x,y))                       # x is 10 y is code
print("x is {new_x} and y is {new_y}".format(new_x=x, new_y=y))    # x is 10 and y is code

# f-string
print('--- f-stirng ---')
teacher_name = "다람쥐"

print(f"안녕하세요. 오늘부터 여러분과 함께 공부할 {teacher_name} 강사입니다~!")
# 안녕하세요. 오늘부터 여러분과 함께 공부할 다람쥐 강사입니다~!

#----------------------------------------------------------------------------------------------
#문자열 인덱싱/슬라이싱
# 파이썬 문자열은 text sequence 형태를 갖는다.
# sequence: 순차적인, 순서가 있는 데이터 구조
# index : 순서(base index == 0)

print('--- 문자열 인덱싱 ---')
x = 'Monday'
print("x의 길이 :", len(x)) # 인덱스 0~5(마지막 인덱스는 len - 1)
print(x[0]) # [] == 배열, [0] == str 배열 중 0번째 인덱스
print(x[1])
print(x[2])
print(x[3])
print(x[4])
print(x[5])

# 역 인데스 : 뒤에서 부터 세는 방법
print(x[-1])
print(x[-2])
print(x[-3])
print(x[-4])
print(x[-5])
print(x[-6])

# str slicing 문자열 일부를 잘라서 가져온다. 원하는 문자열 뒤에 [start:end:step]
# start 시작 인덱스 생략시 0
# end   종료 인덱스로 미포함 생략시 len
# step  건너 뛰는 수로 기본 값 1

print('--- str 슬라이싱 ---')

text = 'Hello World'
print('text :', text)
print(len(text))

print('text[0:5:1] :', text[0:5:1])
print('text[0:5] :', text[0:5])
print('text[:5] :', text[:5])

print('text[6:11] :', text[6:11])
print('text[6:len(text)] :', text[6:len(text)])
print('text[6:] :', text[6:])

print('text[:] :', text[:])

print('text[0:11:2] :', text[0:11:2])
print('text[::2] :', text[::2])

print('text[::-1] :', text[::-1]) #문자열 뒤집기

# 문자형 불변 타입(immutable)
""""
str은 한번 메모라에 저장되면 수정 불가
"""

print('--- 문자열 불변 타입 ---')

s = 'python' # 1790733838704 주소에 'python' 저장
print(s) # s는 저장된 주소에 찾아가서 python을 참조
print('변경 전 s :', id(s)) # id 변수가 저장된 메모리의 주소를 반환
s = s + ' hello' # 변경된 새 주소에 저장
print(s) # 새 주소에서 참조
print('변경 후 s :', id(s)) # 새 주소 반환

# in 연산자 (멤버십 검사 연산자)
# 문자열과 같은 sequence 형태의 타입에 존재 유무 True/False로 반환

print('--- in 연산자 ---')

txt = '김밥, 라면, 어묵, 떡볶이'

print('라면' in txt)

print('돈까스' in txt)



























