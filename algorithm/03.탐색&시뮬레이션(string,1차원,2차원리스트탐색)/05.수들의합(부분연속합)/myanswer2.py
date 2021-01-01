'''

a = data list
n = 8, m = 3 일 때

lt = 현재 선택된 제일 왼쪽의 포인터
rt = 현재 선택된 제일 오른쪽의 포인터

** tot = 연속 부분의 합. 초기화 = a[0]. lt ~ rt-1 까지의 합 **

==> 앞에 설명 듣고 내가 작성한 코드
'''

import sys
sys.stdin = open("./in4.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

lt = 0
rt = 1
total = a[0]
cnt = 0
while rt < n:
    total += a[rt]
    rt += 1
    if total == m:
        cnt += 1
        total -= a[lt]
        lt += 1
    if total > m:
        while total > m:
            total -= a[lt]
            lt += 1
            if total == m : cnt += 1
print(cnt)

file = open("./out4.txt", "rt")
file = int(file.readline())

if cnt == file:
    print('pass')
else: print('fail')
