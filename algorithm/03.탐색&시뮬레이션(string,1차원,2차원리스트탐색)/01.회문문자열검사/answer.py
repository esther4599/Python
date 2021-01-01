# import sys
# sys.stdin = open("./in1.txt", "rt")

n = int(input())
for i in range(n):
    print("#", i+1, sep="", end=" ")
    s = input().upper()
    # 아래와 같이 마지막에 -1을 주면 뒤에서 부터 하나씩 출력
    if s == s[::-1]:
        print("YES")
        continue
    print("NO")
