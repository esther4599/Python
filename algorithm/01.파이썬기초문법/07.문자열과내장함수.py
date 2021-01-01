
# 문자열과 내장함수

msg = "It is time"

# 대문자로 변경
print(msg.upper())

# 소문자로 변경
print(msg.lower())

# 실제 변수에 반영되는 것은 아니다.
print(msg)

tmp = msg.upper()

# find() = 처음 변수 출력
print(tmp.find('T')) # 처음 문자 찾아서 index 출력

# count() = 갯수 확인
print(tmp.count('T'))

# slice
print(msg[:2]) #It
print(msg[3:4]) #i
print(msg[5:]) # time

# len
print(len(msg)) #10

# 배열 처럼 이용
for i in range(len(msg)):
    print(msg[i], end="*")
print()

for i in msg:
    print(i, end="*")
print()

# 내장 함수 : 대소문자 확인
for i in msg:
    if i.isupper(): # islower() == 소문자인지 확인
        print("Capital:", i, end=" ", sep=" ")
print()

# 내장 함수 : isalpha()
for i in msg:
    if i.isalpha():
        print(i, end=" ", sep=" ")
print()

# 아스키코드 값 출력
tmp = 'AZ'
for x in tmp:
    print(ord(x), end=" ")
    print(ord(x.lower()), end=" ")
print()

# 아스키코드 -> 문자
tmp = 65
print(chr(tmp))
