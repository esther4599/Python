import sys
sys.stdin = open("./in5.txt", "rt")
file = int(open("./out5.txt", "rt").readline())

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
k = n//2

answer = 0
for i in range(n):
    for j in range(n):
        if j < k:
            continue
        answer += data[i][j]
        if j >= n-k-1:
            break
    if i < n//2:
        k -= 1
    else:
        k += 1
print(answer)

if file == answer: print("pass")
else: print("fail")