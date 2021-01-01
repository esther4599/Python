
# file에서 데이터 읽어오기
file = open("./testcase/input.txt", "rt")
data = []
while True:
    tmp = file.readline()
    if not tmp: break
    tmp = list(map(int, tmp[:len(tmp)-1].split()))
    data.append(tmp)

file = open("testcase/output.txt", "rt")
answer = []
while True:
    tmp = file.readline()
    if not tmp: break
    tmp = int(tmp[:len(tmp)-1])
    answer.append(tmp)

###################################

# 문제 풀이

for i in range(len(data)):
    print(i, ":", end=" ")
    n = data[i][0]
    k = data[i][1]
    for j in range(1, n+1):
        if n % j == 0: k -= 1
        if k == 0:
            if j == answer[i]: print("pass")
            else: print("fail")
            break
    else:
        if -1 == answer[i]: print("pass")
        else: print("fail")
