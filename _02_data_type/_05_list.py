# sequence type 자료형
# str, list, tuple
# 저장된 값의 순서가 유잗하며 안댁싱과 슬라이싱이 가능
# 순회(iterable) 가능

#  list : 여러 값(literal)을 묶어서 관리(컨테이너 자료형)
# 특징 : 동적으로 크기가 변할 수 있음 (수정 가능)

print('--- list ---')

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple']

print(fruits)
print(fruits[0])
print(type(fruits))
print(type(fruits[0]))
print(len(fruits))
print(len(fruits[4]))

# list 저장 요소 추가, 수정, 삭제
# list는 동적으로 크기 변경이 가능한 mutable 자료형이다.
# mutable : list, st, dict
# immutable : int, float, bool, str, tuple

print('--- list mutable check---')
print("추가 전 fruits:", fruits)
print("추가 전 id:", id(fruits))
before = id(fruits)

# list.append(값) : list 마지막에 값을 추가

fruits.append('banana')
print("추가 후 fruits:", fruits)
print("추가 후 id:", id(fruits))
after = id(fruits)
print('append 전과 후 같은 리스트인가:', before == after)

# list.insert(index,값): 원한는 인덱스 위치에 값을 삽입하며 이후 요소들의 인덱스 값이 1씩 증가

fruits.insert(1, 'watermelon')
after = id(fruits)
print(fruits)
print(id(fruits))
print('append 전과 후 같은 리스트인가:', before == after)

# liss[idx] = 값 : list 인덱스 값을 수정

fruits[2] = 'strawberry'
after = id(fruits)
print(fruits)
print(id(fruits))
print('append 전과 후 같은 리스트인가:', before == after)

# 특정 인덱스 값 제거
# list.pop(idx) 특정 인덱스 값 제거, 기본 값 0, 제거된 인덱스 뒤 요소들의 인덱스 값 -1

print('--- list pop ---')
fruits.pop(3)
after = id(fruits)
print(fruits)
print('append 전과 후 같은 리스트인가:', before == after)

# list.remove(값) 리스트 내의 값을 모두 제거

print('--- list remove ---')
fruits.remove('apple')
after = id(fruits)
print(fruits)
print('append 전과 후 같은 리스트인가:', before == after)

# 2차원 리스트

students = [
    ['홍길동', 30],
    ['이순신', 80],
    ['세종대왕', 100]
]

print(students)
print(students[0])
print(students[0][1])
print(students[0][0])

print(len(students))
print(len(students[0]))


# str.split(구분자): 구분자를 기준점으로 분리하여 list 형태로 반환
#csv(Comma Separated Value)

data = '홍길동,20살,서울시,서초구'

data_split = data.split(',')
print(data_split)
print(type(data_split))

# list 슬라이싱(str 슬라이싱과 동일)

print('--- list slicing ---')

texts = ['hello', '안녕', '아리가또', 'hi']

print(texts[:2]) # hello 안녕
print(texts[1:3]) # 안녕, hi
print(texts[1:3][::-1]) #hi 안녕
print(texts[2:0:-1]) #hi 안녕


# slicing을 이용한 list 값 변경
print(texts)
texts[:2] = ['aaa', 'bbb']
print(texts)

texts[1:3] = ['ccc', 'ddd']
print(texts)

print('--- list 더하기 연산 ---')
a = [10, 20]
b = [30, 40]
a = a + b
print(a)
b = b + a
print(b)

# list 순회(iterable) 반복 가능

print('--- list 순회 ---')

lst = ['a', 'b', 'c']

# list 요소 순회

for i in lst:
    print(i)

# 인덱스 같이 보기

for idx, i in enumerate(lst):
    print(f'lst[{idx}]: {i}')


# list api

print('--- list.count(값) ---') # list 내부에 같은 값이 몇 개 존재하는가
fruits = ['apple', 'banana', 'cherry', 'melon', 'kiwi']

print('fruits.count(apple):', fruits.count('apple'))
print('fruits.count(banana):', fruits.count('banana'))
print('fruits.count(kiwi):', fruits.count('kiwi'))

# sort : 정렬
# list.sort() : 원본 리스트 내에서(in-place) 정렬
# 원본 데이터 손실

# sorted(list) : 원본을 복사하여 새 리스트에(not-in-place) 정렬
# 원본 데이터 유지

print('--- list.sort ---')

nums = [100, 30, 50, 20, 70]
print(nums)
nums.sort()
print('오름차순 정렬된 nums:', nums)
nums.sort(reverse=True)
print('내림차순 정렬된 nums:', nums)

# key 속성 -> 정렬 기준 부여 가능
print('--- key 속성 -> 정렬 기준 함수 ---')
print('fruits :" fruits')

#len 기준 정렬
fruits_1 = sorted(fruits, key=lambda x: len(x))
print('fruits:', fruits_1)

fruits_2 = sorted(fruits, key=lambda x: len(x), reverse=True)
print('fruits:', fruits_2)

fruits.sort(key=len)
print('fruits:', fruits)


# 커스텀 정렬기준함수
def my_sort(elem):
    return len(elem), elem # tuple로 우선순위 지정

fruits.sort(key=my_sort)
print(fruits)

# list unpacking
# list == 변수의 묶음(packing)
print('--- list unpacking ---')
numbers = [10, 20, 30,]

# a = numbers[0]
# b = numbers[1]
# c = numbers[2]

a, b, c = numbers
print(a, b, c)

d, *e = numbers
print(d, e)

numbers = [10, 20, 30, 40, 50]

a, *b, c = numbers
print(a, b, c)








