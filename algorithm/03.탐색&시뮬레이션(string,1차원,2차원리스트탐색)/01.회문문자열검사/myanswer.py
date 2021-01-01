# import sys
# sys.stdin = open("./in5.txt", "rt")

n = int(input())
for test in range(n):
    print("#", test+1, sep="", end=" ")
    data = input().lower()
    x = len(data)
    for i in range(x//2):
        # data[-1] = 마지막 문자, data[-2] = 뒤에서 두번째 문자
        # if not (data[i] == data[x-i-1]):
        if not (data[i] == data[-1-i]):
            break
    else:
        print("YES")
        continue
    print("NO")
