'''
2 ~ n 까지 소수인지 확인하기
만약 소수이면 해당 소수의 배수는 다 방문 처리
방문 처리가 안된 수를 기준으로 소수인지 확인
'''

n = int(input())

check = [True] * (n+1)
answer = 0
for i in range(2, n+1):
    if not check[i]:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            break
    else:
        answer += 1
        j = i
        while j < n+1:
            check[j] = False
            j *= i
print(answer)