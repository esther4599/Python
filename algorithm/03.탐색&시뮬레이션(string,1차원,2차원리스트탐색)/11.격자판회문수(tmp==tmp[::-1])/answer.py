import sys
sys.stdin = open("in5.txt", "rt")
file = int(open("out5.txt").readline())

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(3):
    for j in range(7):
        tmp = board[j][i:i + 5]
        # slicing 이용해서 역순으로 만들기
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if board[i + k][j] != board[i + 5 - k - 1][j]:
                break;
        else:
            cnt += 1

print(cnt)

if cnt == file: print('pass')
else: print('fail')
