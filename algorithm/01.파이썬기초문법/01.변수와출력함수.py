
# 값 교환
a, b = 10, 20
b, a = a, b
print(a, b) # 20 10 출력


# 변수 타입
a = 12345
print(type(a)) # <class 'int'>

a = 12.123456789123456789
print(a) # 12.123456789123457 float=8byte
print(type(a)) #<class 'float'>

a = "stu"
print(type(a)) # <class 'str'>

#출력 함수
a,b,c = 1,2,3
print(a,b,c, sep='') # 123 출력 sep=변수를 이을 때 설정

print(a, end=' ')
print(b, end=' ')
print(c, end='\n')
# => 3 변수가 "1 2 3" 출력