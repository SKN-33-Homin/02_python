# 논리형 (boolean) True or False
from sockshandler import socks4_no_rdns

a = True
b = False

print(a)
print(b)
print(type(a))
print(type(b))
print(int(a))
print(int(b))

# 비교 연산
"""
>, >=, <, <=, ==, !=

A > B 맞으면 True, 틀리면 False
A >= B : 크거나 같다
A == B : 같다
A != B : 같지 않다

"""

print("1 > 0.5:", 1 > 0.5) #True
print("1 < 0.5:", 1 < 0.5) #False
print("1 >= 0.5:", 1 >= 0.5) #True
print("1 <= 0.5:", 1 <= 0.5) #False
print("1 == 1:", 1 == 1) #True
print("1 != 1:", 1 != 1) #False

# 논리 부정 연산 (not)

print(True)
print(False)
print(not True)
print(not False)
print(not not True)
print(not not False)

# and 연산 - A 와 B 모두 참인 경우 True

"""
T & T == T
T & F == F
F & T == F
F & F == F
F가 나올 경우 and 연산은 바로 F
"""

print('---- and ----')
print(True and True) #True
print(True and False) #False
print(False and True) #False
print(False and False) # False

# or 연산 - A 또는 B 둘 중 하나 이상 참이면 True

"""
T || T == T
T || F == T
F || T == T 
F || F == F
T가 나올 경우 or 연산은 바로 T
"""

print('---- or ----')
print(True or True) #True
print(True or False) #True
print(False or True) #True
print(False or False) #False

# 60점 이상 시 합겨(True), 아닐 시 불합격(False)
print('--- 합/불 ---')
score = int(input("점수를 입력하세요.")) # int() : str -> int, input() : str로 저장

result = score >= 60

# print(result)
print('합격 여부 :', "합격" if result == True else '불합격')

# not 연산 - 우항에 있는 비교 연산 결과 또는 논리 자료형을 뒤집는다. 즉, True가 오면 False를, False가 오면 True를 반환한다.
"""
not T = F
not F = T
print(not 'ohgiraffers' == 'Ohgiraffers')    # True
"""

print('---- not ----')
print(not True) #False
print(not False) #True
