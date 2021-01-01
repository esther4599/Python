import sys

'''
match 함수 정리
ceil() 올림
floor() 내림
fabs() float 형으로 절대값 반환
-----------
파이썬 내장 함수
round() 반올림
abs() 절대값 반환
'''

for test in range(1,6):
    sys.stdin = open("./testcase/in"+str(test)+".txt", "rt")
    n = int(input())
    data = list(map(int, input().split()))
    avg = int(round(sum(data)/len(data), 0))

    check = []
    for i in range(len(data)):
        check.append(abs(avg-data[i]))

    m = min(check)
    M = max(check)
    result = {}
    while True:
        if min(check) != m: break
        key = check.index(m)
        check[key] = M
        result[key] = data[key]

    data = set()
    for i in result.values():
        data.add(i)
    data = list(data)
    data.sort(reverse=True)

    check = list(result.keys())
    check.sort()

    print(avg, end=" ")
    b = False
    for i in data:
        for j in check:
            if result[j] == i:
                print(j+1)
                b = True
                break
        if b: break