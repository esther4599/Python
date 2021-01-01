# import sys
# sys.stdin = open("./in5.txt", "rt")

def checkGroup(a):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            c = [0]*10
            for k in range(3):
                for l in range(3):
                    if c[a[i+k][j+l]] == 1:
                        return False
                    c[a[i + k][j + l]] += 1
    return True

def checkLine(a):
    for i in a:
        if sum(i) != 45:
            return False
    return True

data = [list(map(int, input().split())) for _ in range(9)]
answer = "NO"
if checkGroup(data):
    if checkLine(data):
        data = list(zip(*data))
        if checkLine(data):
            answer = "YES"
print(answer)