
''' n이 커지면 실행 시간이 너무 길어진다 '''
n = int(input())

answer = 0
for i in range(2, n+1):
    for j in range(2, int(i*0.5)+1):
        if j == 1: continue
        if i % j == 0:
            break
    else: answer += 1
print(answer)
