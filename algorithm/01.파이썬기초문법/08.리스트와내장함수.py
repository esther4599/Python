
# random 이용
import random as r

#################################################

# 1. list?

a = [] # list
b = list()
print(a,b, type(a), type(b)) # [] [] <class 'list'> <class 'list'>

b = list(range(1,11))
print(b)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = [range(11,15)] # a = [range(11, 15)]
a = [11, 12, 13, 14]
c = b+a # 리스트가 합쳐진다.
print(c) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#################################################

# 2. list 내장함수

a = list(range(1,6))
print(a)

# 인자 추가  append(value) / insert(index, value)
a.append(6)
print(a)

a.insert(3, "hello") # 매개변수: index, value = index 위치에 value 저장
print(a)

# 인자 삭제 pop(index) / remove(value)
print(a.pop()) # pop() : default = 마지막 인자
print(a)
print(a.pop(3)) # 매개변수 : index = 3
print(a)

a.append(4) # [1, 2, 3, 4, 5, 4]
print(a.remove(4)) # None = return 안한다.
print(a) # [1, 2, 3, 5, 4] = 앞에서 부터 search, 첫 value만 삭제


# index() 찾기
print(a.index(5)) # 3

# sum()
a = list(range(1,11))
print(a)
print(sum(a))

# max() / min()
print(max(a))
print(min(a))

# shuffle()
r.shuffle(a) # random으로 섞기
print(a) # [10, 6, 4, 3, 9, 5, 7, 2, 8, 1]

# sort() / reverse 조건 이용하기
a.sort()
print(a)

a.sort(reverse=True)
print(a) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

a.reverse()
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# clear
a.clear()
print(a)
