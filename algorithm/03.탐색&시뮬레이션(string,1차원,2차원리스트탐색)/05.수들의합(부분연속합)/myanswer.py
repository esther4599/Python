import sys
sys.stdin = open("./in5.txt", "rt")

n, m = map(int, input().split())
data = list(map(int, input().split()))

cnt = 0
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += data[j]
        if sum == m: cnt += 1
        elif sum > m: break
print(cnt)

file = open("./out5.txt", "rt")
file = int(file.readline())

if cnt == file:
    print('pass')
else: print('fail')
