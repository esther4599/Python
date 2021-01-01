
'''
최솟값을 구하는 코드
'''

arr = [5, 3, 7, 9, 2, 5, 2, 6]

# 자료형의 최댓값 저장
arrMin = float('inf')
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin) # 2

#######################################

'''
최댓값을 사용하지 않고도 코드를 구현할 수 있다.
'''

arr = [5, 3, 7, 9, 2, 5, 2, 6]

arrMin = arr[0]
for i in range(1, len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i]
print(arrMin) # 2