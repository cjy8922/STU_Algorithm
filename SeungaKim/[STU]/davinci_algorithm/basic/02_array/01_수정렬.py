# 2750 수 정렬하기
'''
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''
# starts 1:45
nums = int(input())

def sorting_nums(nums) :
    arr = []
    for i in range(nums):
        # assign user inputs(integer)
        user_input = int(input())
        arr.insert(i, user_input)
    # for j in range(nums-1):
    #     if arr[j] > arr[j+1]:
    #         arr[j], arr[j+1] = arr[j+1], arr[j]
    arr.sort()
    return arr

# print(f'arr = {sorting_nums(nums)}')
sorted_arr = sorting_nums(nums)
for i in range(len(sorted_arr)):
    print(sorted_arr[i])
# ends 1:55