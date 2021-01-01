import sys
sys.stdin = open("in5.txt", "rt")

n = int(input())
answer = 0
for test in range(n):
    data = list(map(int, input().split()))

    result = 0
    value = max(data)
    type = 1

    for i in range(3):
        cnt = 0
        for j in range(3):
            if data[i] == data[j]:
                cnt += 1
        if cnt > type:
            type = cnt
            value = data[i]

    if type == 3:
        result = 10000 + value * 1000
    elif type == 2:
        result = 1000 + value * 100
    else:
        result = value * 100

    if answer < result:
        answer = result
print(answer)