# 논리형 (boolean) True or False

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