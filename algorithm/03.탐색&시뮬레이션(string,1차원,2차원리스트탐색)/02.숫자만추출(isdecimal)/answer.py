import sys
sys.stdin = open("./in1.txt", "rt")

s = input()
res = 0
for i in s:
    if i.isdecimal():
        res = res*10 + int(i)
print(res)

cnt = 0
for i in range(1, res+1):
    if res%i == 0:
        cnt += 1
print(cnt)