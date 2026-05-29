# number (숫자형)
"""
정수, 실수 복소수

type(변수명 | 값) 함수 : 변수 값의  타입 확인 내장 함수
"""


# 정수 (int)

n = 123

print(n, type(n))

price = 1_000_000_000

print(price, type(price))

# 정수의 최댓값

import sys

print(sys.maxsize, type(sys.maxsize))

# 2진법, 8진법, 16진법

a = 0b100
print(a, type(a))

b = 0o23

print(b, type(b))

c = 0xff

print(c, type(c))

# 실수 (float) 소수의 경우 근사치 소수를 표현

m = 123.456

print(m, type(m))


# 복소수 (complex) j로 표시

c = 2j

print(c, type(c))

d = 3 + 4j

print(d, type(d))

# 연산
"""
+
-
*
/
//      몫
%(mod)  나머지
**      거듭제곱
"""

print((1+2), (1-2), (1*2), (1/2), (1//2), (1%2), (12**2))




