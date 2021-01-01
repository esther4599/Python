import sys
sys.stdin = open("./in5.txt", "rt")
file = open("./out5.txt", "rt")

data = [i for i in range(21)]

for i in range(10):
    s, e = map(int, input().split())
    tmp = data[s:e+1]
    tmp = list(reversed(tmp))
    data[s:e+1] = tmp

for i in data[1:]:
    print(i, end=" ")
print()

answer = list(map(int, file.readline().split()))

if answer == data[1:]:
    print('pass')
else: print("fail")
