def reverse(x):
    tmp = ""
    for i in x:
        tmp = i + tmp
    return int(tmp)

def isPrime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            break
    else: return True
    return False

n = int(input())
data = input().split()
for i in data:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end=" ")
print()
