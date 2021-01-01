
# sort 함수의 경우 nlogn 시간복잡도를 갖는다.
# 배열의 총 길이가 8이면 8log8

'''
문제의 경우 각 배열의 값들이 정렬되어서 입력된다. 따라서 sort()를 사용하지 않는 것이 더 효율적일 수 있다.
본 알고리즘에서는 n 시간 복잡도를 갖는다.
'''

import sys
sys.stdin = open("./in5.txt", "rt")

n = int(input())
ndata = list(map(int, input().split()))

m = int(input())
mdata = list(map(int, input().split()))

p1, p2 = 0, 0 # ndata와 mdata의 현재 포인터를 가르키는 포인터
answer = []
while p1 < n and p2 < m:
    if ndata[p1] >= mdata[p2]:
        answer.append(mdata[p2])
        p2 += 1
    else:
        answer.append(ndata[p1])
        p1 += 1

if p1 == n:
    answer += mdata[p2:]
else:
    answer += ndata[p1:]
print(answer)

file = open("./out5.txt", "rt")
file = list(map(int, file.readline().split()))
if answer == file:
    print('pass')
else: print('fail')
