
# 1부터 N까지 홀수 출력
a = int(input("N : "))

for i in range(1,a+1):
    if i % 2 == 1:
        print(i, end=" ")
print()

######################################

# 1부터 N까지 합 구하기
a = int(input("N : "))
print(sum(range(1, a+1)))

# 강사님 풀이
n = int(input())
sum = 0

for i in range(1,n+1):
    sum += i
print(sum)

######################################

# N의 약수 출력하기
a = int(input("N : "))
for i in range(1,int(a**0.5)+1):
    if a % i == 0:
        print(i, end=' ')
print()
