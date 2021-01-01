
# 함수
def add01(a,b):
    c = a+b
    print(c)

add01(2,3)
add01(3,5)

###########################

# return

def add02(a,b):
    c = a+b
    return c

print(add02(2,3))
print(add02(3,5))

###########################

# return 여러개 = tuple로 반환

def cal(a,b):
    c = a+b
    d = a-b
    return c, d

print(cal(5, 1)) # (6, 4)

answer = cal(5,1)
print("+ : ", answer[0], ", - : ", answer[1], sep="")

###########################

# 소수만 출력하는 함수 만들기

a = [12, 13, 7, 9, 19]

def prime (data):
    answer = list()
    for d in data:
        check = True
        for i in range(2,int(d**0.5)+1):
            if d % i == 0:
                check = False
                break
        if check:
            answer.append(d)
    return answer
print(prime(a))
