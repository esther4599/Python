import sys
sys.stdin = open("./in5.txt", "rt")
file = int(open("./out5.txt", "rt").readline())

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for _ in range(m):
    target, dir, k = map(int, input().split())
    k = k % n

    if dir == 0:
        data[target-1] = data[target-1][k:] + data[target-1][:k]
        continue
    data[target-1] = data[target-1][n-k:] + data[target-1][:n-k]

s = 0
e = n
answer = 0
for i in range(n):
    for j in range(s, e):
        answer += data[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(answer)

if file == answer: print("pass")
else: print("fail")
