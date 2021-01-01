import sys
sys.stdin = open("./in5.txt", "rt")
file = int(open("./out5.txt", "rt").readline())

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    data[i] = [0] + data[i] + [0]
data.insert(0, [0]*(n+2))
data.append([0]*(n+2))

check = list([False]*(n+2) for _ in range(n+2))

cnt = 0
dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(1, n+1):
    for j in range(1, n+1):
        if check[i][j]: continue

        tmp = data[i][j]
        check[i][j] = True
        for x, y in dir:
            if tmp <= data[i+x][j+y]:
                break
        else:
            cnt += 1
            for x, y in dir:
                check[i + x][j + y] = True
print(cnt)

if file == cnt: print("pass")
else: print("fail")



