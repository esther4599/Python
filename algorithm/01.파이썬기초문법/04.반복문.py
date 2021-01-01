
# range() => 시작은 포함, 끝은 제외
a = range(10)
print(list(a))

a = range(1,11)
print(list(a))

######################################

# 반복문 for
for i in range(1,11):
    print(i, end=" ")
print()
# => 1 2 3 4 5 6 7 8 9 10

for i in range(10,0,-1):
    print(i, end=" ")
print()
# => 10 9 8 7 6 5 4 3 2 1

######################################

# for else 문
for i in range(1,11):
    print(i, end=" ")
    if i == 5:
        break
else:
    print(11)
print()
# for 문이 정상 종료되지 않으면 11이 출력되지 않는다.

for i in range(1,11):
    print(i, end=" ")
    if i == 5:
        continue
else:
    print(11)
print()
# 11이 출력된다.

######################################

# 반복문 while
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
print()
