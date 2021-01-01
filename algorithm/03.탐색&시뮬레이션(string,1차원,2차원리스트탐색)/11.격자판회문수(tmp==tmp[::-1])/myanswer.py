import sys
sys.stdin = open("in5.txt", "rt")
file = int(open("out5.txt").readline())

data = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(7):
    for j in range(7):
        if i + 4 < 7:
            for k in range(2):
                if data[i+k][j] != data[i+4-k][j]:
                    break
            else: cnt += 1

        if j + 4 < 7:
            for k in range(2):
                if data[i][j+k] != data[i][j+4-k]:
                    break
            else: cnt += 1
print(cnt)

if cnt == file: print('pass')
else: print('fail')
