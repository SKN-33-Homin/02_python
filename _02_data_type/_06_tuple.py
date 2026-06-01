# tuple: () 이용하는 불변(immutable)
# sequence 타입 (indexing, slicing, iterable)
# 주로 함수 반환값이며 변경되면 안되는 집합을 만들 경우 사용

print("--- tuple ---")

t1 = () # 빈 tuple
t2 = (10) # == (int)10
print(t1, t2)
print(type(t1), type(t2))
t3 = (10,) # == (tuple) (10,)
print(t3)
print(type(t3))
t4 = (10,20) # == (tuple) (10, 20)
print(t4)
print(type(t4))
t5 = 10,20,30 # ()를 생략한 tuple
print(t5)
print(type(t5))

# tuple indexing, 수정 불가(읽기 전용)

tpl = 'a', 'b', 'c', 'd'
print(tpl[0], tpl[1], tpl[2], tpl[3])

# tuple slicing

print('--- tuple slicing ---')

print(tpl[0:2])
print(tpl[1::2])

# tuple unpacking

print('--- tuple unpacking ---')

q,w,e,r = tpl
print(q,w,e,r)

*r, t = tpl
print(r, t)
print(type(r), type(t))

# tuple 이용한 변수 값 할당

print('--- tuple 변수 값 할당 ---')

num1, num2 = 100,200 # () 생략
print(num1, num2)

print("--- tuple을 이용한 값 교환 ---")

num2, num1 = num1, num2

print(num1, num2)

