
n, m = map(int, input().split())

data = [0] * (n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        data[i+j] += 1

M = max(data)
for i in range(len(data)):
    if data[i] == M:
        print(i, end=" ")
print()

###############################

''' max 찾는 코드 '''

max = -2160000000
for i in range(len(data)):
    if max < data[i]:
        max = data[i]