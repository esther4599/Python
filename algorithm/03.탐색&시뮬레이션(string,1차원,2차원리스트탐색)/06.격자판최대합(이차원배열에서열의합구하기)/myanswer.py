'''
    이차원 배열의 특정 열의 합을 구하는 방법
    1. inline for 이용
        b[i] for b in data

    2. zip() 함수 이용
    => 적용된 방법
'''

import sys
sys.stdin = open("./in5.txt", "rt")
file = open("./out5.txt", "rt")

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
atad = list(zip(*data))

answer = 0

diagonal1 = 0 # 좌 -> 우
diagonal2 = 0 # 우 -> 좌
for i in range(n):
    tmp = max(sum(data[i]), sum(atad[i]))
    if tmp > answer: answer = tmp
    diagonal1 += data[i][i]
    diagonal2 += data[i][n-1-i]

if int(file.readline()) == max(answer, diagonal1, diagonal2):
    print("pass")
else: print("fail")
