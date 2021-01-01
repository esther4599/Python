import sys
sys.stdin = open("./in1.txt", "rt")
file = int(open("./out1.txt", "rt").readline())

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]


# 위아래에 [0] 리스트 추가
a.insert(0, [0]*n)
a.append([0]*n)

# 좌우에 [0] 리스트 추가
for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1
print(cnt)

if file == cnt: print("pass")
else: print("fail")