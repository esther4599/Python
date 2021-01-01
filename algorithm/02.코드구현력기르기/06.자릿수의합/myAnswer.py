def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum

n = int(input())
data = list(map(int, input().split()))

max = digit_sum(data[0])
answer = data[0]
for i in range(1, n):
    tmp = digit_sum(data[i])
    if max < tmp:
        max = tmp
        answer = data[i]
print(answer)