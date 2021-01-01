
'''
python의 round 함수는 round_half_even 방식을 채택한다.
정확한 half의 경우 짝수값으로 반올림한다.
round(4.5000) == 4
round(5.5000) == 6

흔히 우리가 아는 반올림은 round_half_up 방식으로
4이하 = 버림, 5이상 = 올림
'''

import sys

for test in range(1,6):
    sys.stdin = open("./testcase/in"+str(test)+".txt", "rt")
    n = int(input())
    a = list(map(int, input().split()))

    '''round_half_even 문제로 아래 코드 수정'''
    # ave = round(sum(a)/n, 1)
    ave = int(sum(a)/n+0.5)

    min = 2147000000
    score = -1
    res = -1
    for idx, x in enumerate(a):
        tmp=abs(x-ave)
        if tmp < min:
            min = tmp
            score = x
            res = idx + 1
        elif tmp == min:
            if score < x: # 답이 동일한 경우는 변경되지 않음으로 번호가 제일 작은 학생이 출력된다.
                score = x
                res = idx + 1
    print(score, res)
