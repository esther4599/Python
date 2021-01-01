def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum

n = int(input())
data = list(map(int, input().split()))

max = digit_sum(data[0])
res = data[0]
for i in range(1,n):
    tot = digit_sum(data[i])
    if tot > max:
        max = tot
        res = data[i]
print(res)