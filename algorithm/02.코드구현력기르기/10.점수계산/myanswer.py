import sys
sys.stdin = open("in5.txt", "rt")

n = int(input())
data = list(map(int, input().split()))

score = 0
cnt = 1
for i in range(n):
    if data[i] == 0:
        cnt = 1
    else:
        score += cnt
        cnt += 1
print(score)
