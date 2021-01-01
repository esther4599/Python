'''
강의에 나온 set 정리 + 적용하기

set = 중복을 허용하지 않는 자료구조. 순서가 존재하지 않는다.
'''

import sys
import itertools
for test in range(1,6):
    sys.stdin = open("./testcase/in"+str(test)+".txt", "rt")
    n, k = map(int, input().split())
    data = list(map(int, input().split()))

    result = set() # set 생성
    for i in itertools.combinations(data, 3):
        result.add(sum(i))

    # set은 순서가 없어 정렬을 할 수 없으므로 자료구조 list로 변경
    result = list(result)
    result.sort(reverse=True)

    file = open("./testcase/out"+str(test)+".txt", "rt")
    if result[k-1] == int(file.readline()):
        print("pass")
    else: print("fail")
