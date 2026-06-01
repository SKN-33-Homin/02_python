# {} set 중복 하욕 X, 시퀀스 앙비 X, iterable은 가는, 집합 관련 메소드 제동

print('--- set ---')
st = {1,2,3,4,2,3,1,2,3,4,3,2,3}
print(st, type(st))

print(" list => set() 변경(중복 제거)")
lst = [1,2,5,2,3,1,5,5]
st2 = set(lst)

print(st2, type(st2))

print("--- set -> list")
lst2 = list(st2)
print(lst2, type(lst2))

print(" tuple => set() 변경(중복 제거)")
tpl = (1,2,5,2,3,1,5,5)
st3 = set(tpl)
print(st3, type(st3))

# 요소 추가(add)
print('--- 요소 추가 ---')
my_nums = {20, 30, 40}
my_nums.add(10)
print(my_nums)

# 요소 제거(remove)
my_nums.remove(10)
print(my_nums)

#전체 제거(clear)
my_nums.clear()
print(my_nums)

# set 순회
my_nums = {30, 50, 70, 90}
for num in my_nums: # my_nums의 요소를 num에 저장
    print(num)

# 집합 연산

print('--- set 집합연산 ---')
m = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
n = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}

print('합집합: ', m.union(n))
print('교집합: ', m.intersection(n))
print('차집합: ', m.difference(n))
print('대칭차집합: ', m.symmetric_difference(n)) # 합집합 - 교집합











