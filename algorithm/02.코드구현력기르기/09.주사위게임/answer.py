import sys
sys.stdin = open("in4.txt", "rt")

n = int(input())
answer = 0

for i in range(n):
    tmp = input().split()
    tmp.sort() # 내장함수 이용해 정렬
    a, b, c = map(int, tmp)

    money = 0
    if a==b and b ==c: # 눈이 모두 같은 경우
        money = 10000+a*1000
    # 2개의 눈이 같은 경우
    elif a==b or a==c:
        money = 1000 + 100 * a
    elif b==c:
        money = 1000 + 100 * b
    else:
        money = 100 * c

    if answer < money:
        answer = money

print(answer)