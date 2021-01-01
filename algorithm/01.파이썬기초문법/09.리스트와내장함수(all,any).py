
a = [23, 12, 36, 53, 19]

print(a[:3]) # [23, 12, 36]

print(a[1:4]) # [12, 36, 53]

print(len(a))

#################################################

for i in range(len(a)):
    print(a[i], end=" ")
print()

for i in a:
    print(i, end=" ")
print()

#################################################

# enumerate() => 코테에서 사용하면 실행시간이 오래 걸린다.

for i in enumerate(a):
    print(i, end=" ")
print() # (0, 23) (1, 12) (2, 36) (3, 53) (4, 19)

# () = tuple 변경이 불가능
for i in enumerate(a):
    print("index:", i[0], end=" ")
    print("value:", i[1])

for index, value in enumerate(a):
    print(index, value, sep=": ")

#################################################

# all 함수 = and

if all(60 > x for x in a): print("success")
# success

if all(53 > x for x in a): print("success")
else: print("fail")
# fail

#################################################

# any() = or

if any(53 > x for x in a): print("success")
else: print("fail")
# success
