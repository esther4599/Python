
# 람다 함수

# 일반 함수
def plus_one(x):
    return x+1

print(plus_one(1)) # 2

# 람다 함수 = 변수에 저장을 해야 한다.
plus_two = lambda x: x+2

print(plus_two(1)) # 3

# 실제 적용
a = [1, 2, 3]
print(a) # [1, 2, 3]
print(list(map(plus_two, a))) # [3, 4, 5]
print(list(map(lambda x : x+2, a))) # [3, 4, 5]
