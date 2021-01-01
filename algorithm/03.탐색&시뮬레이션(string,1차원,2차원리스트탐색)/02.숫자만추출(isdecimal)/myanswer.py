# import sys
# sys.stdin = open("./in5.txt", "rt")

data = input()
num = ""
for i in data:
    # isdigit() = 숫자로 된 문자열인지 확인, isdecimal() = 0~9 숫자,
    # isnumeric() = 1/2 도 숫자로 인정된다.
    if i.isdecimal():
        num += i
num = int(num)
print(num)

cnt = 0
for i in range(1, int(num**0.5)+1):
    if num % i == 0:
        cnt += 1
        if num//i != i:
            cnt += 1
print(cnt)
