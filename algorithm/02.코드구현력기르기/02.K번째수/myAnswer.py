import sys

for test in range(1,6):
    sys.stdin = open("./testcase/in"+str(test)+".txt", "rt")
    T = int(input())
    for i in range(1, T+1):
        print("#", i, sep="", end=" ")
        n, s, e, k = map(int, input().split())

        data = list(map(int, input().split()))
        data = data[s-1:e]
        data.sort()
        print(data[k-1])
    print("================")
