import sys
sys.stdin = open("./in5.txt", "rt")
file = int(open("./out5.txt", "rt").readline())
'''
s와 e변수 주기

처음에는 s=e=n//2
다음에는 s = s-1, e = e+1
==> 행이 n//2보다 큰 경우까지

이후
s = s+1, e = e-1
'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0

s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)

if file == res: print("pass")
else: print("fail")