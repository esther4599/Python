
# 변수입력
a = input("숫자를 입력하세요 : ")
print(a)
print(type(a)) # <class 'str'>

a, b = input("숫자 입력 : ").split() # 띄어쓰기로 변수를 구분해서 입력받는다.
print(a, b)
print(a+b) #23

# 형 변환 int()
a = int(a)
b = int(b)
print(a+b)

# 형 변환 map() 앞 = 함수, 뒤 = 데이터
a, b = map(int, input("숫자 입력 : ").split())
print(a+b)

#########################################

# 연산자

a, b = 9, 2
print(a//b) # 몫
print(a/b) # 나누기 => 실수 return
print(a%b) # 나머지
print(a**b) #a^b = 81