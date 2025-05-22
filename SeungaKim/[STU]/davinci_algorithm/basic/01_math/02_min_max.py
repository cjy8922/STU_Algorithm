'''
    [02] 최댓값, 최솟값 구하기
    우리는 여러 가지 조건이 있을 때 최고의 선택을 하려고 합니다. 
    가령 집에서 학교까지 가는 여러 가지 방법 중 가장 빠른 시간에 갈 수 있는 방법을 찾기도 하고, 가장 거리가 짧은 경로를 찾기도 합니다.
    비슷한 용도의 여러 가지 제품이 있으면 그중 가장 가성비가 좋은 제품을 사던가, 가장 싼 제품을 사기도 합니다. 
    이처럼 기준이 다를 뿐 최댓값을 찾던지, 최솟값을 찾는 것에 익숙해져 있습니다. 
    그럼, 직접 최솟값이나 최댓값을 찾는 방법을 알아보겠습니다
    
    (1) 함수 이용하기
    (2) 반복문 이용하기
    (3) 숫자 범위 고려하기
'''
# (1) 함수 이용하기
# print("Type any random numbers with a single space in an array")
# arr = list(map(int, input().split()))

# print(min(arr))
# print(max(arr))

# (2) 반복문 이용하기
# print("Type any random numbers with a single space in an array")
# arr = list(map(int, input().split()))

# min = arr[0]
# max = arr[0]
# for i in range(len(arr)):
#     if min > arr[i]:
#         min = arr[i]
#     if max < arr[i]:
#         max = arr[i]

# print(min)
# print(max)        

# (3) 숫자 범위 고려하기 : what if numbers less than zero?
# arr = list(map(int, input().split()))

# filtered_arr = [i for i in arr if i >= 0]

# min = filtered_arr[0]
# max = filtered_arr[0]

# for i in filtered_arr: # to avoid neg nums as setting the range for pos integer
#     if min > i :
#         min = i
#     if max < i:
#         max = i
        
# print(min)
# print(max)

'''
TL;DR:
case(1): for i in arr == loop over values, 3 6 9 7
case(2): for i in range(len(arr)) == loop over indices, 0 1 2 3 
'''

###
'''
문제  # 10818
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
모든 정수는 -1,000,000보다 크거나 같고, 
1,000,000보다 작거나 같은 정수이다.
'''
num_in_arr = int(input())
arr = list(map(int, input().split()))

min = arr[0]
max = arr[0]

if num_in_arr != len(arr):
    print("Invalid nums of elements in the array.\nExit the program.")
    exit()

for i in arr:
    if min > i:
        min = i
    if max < i :
        max = i

print(min , max)