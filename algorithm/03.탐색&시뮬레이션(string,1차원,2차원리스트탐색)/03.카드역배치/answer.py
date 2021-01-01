import sys
sys.stdin = open("./in1.txt", "rt")
file = open("./out1.txt", "rt")

a = list(range(21))

for _ in range(10): # 변수가 필요없다면 _로 작성한다.
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]

a.pop(0) #pop() 매개변수로 원하는 index를 입력할 수 있다.
for i in a:
    print(i, end=" ")
print()

answer = list(map(int, file.readline().split()))
if answer == a[1:]:
    print('pass')
else: print("fail")
