
n = int(input())
data = list(map(int, input().split()))

m = int(input())
data += list(map(int, input().split()))

data.sort()
for i in data:
    print(i, end=" ")
print()
