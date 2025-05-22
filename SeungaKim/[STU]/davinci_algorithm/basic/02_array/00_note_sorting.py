# 1. SELECTION SORT
# find max or min value to swap

'''# arr = [3, 2, 5, 6, 1]
# arr = list(input("enter the list you want to sort >>"))
arr = list(map(int, input("Enter the numbers in the list you wanted to sort(seperated by spaces) >> ").split()))

def selection_sort(arr):
    n = len(arr)    # check length of the array
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
            # else, do nothing
        arr[i], arr[min_index] = arr[min_index], arr[i] # temp 안쓰네?
        print(f'{i+1} 번째 정렬 후 = {arr}')
    return arr

# print out the output
print(f'after sorting >> {selection_sort(arr)}')'''


# 2. BUBBLE SORT
# 앞에서부터 두 수 비교 -> 큰 수를 맨 뒤로 보냄(n)
# 두번째 라운드 : 앞에서부터 두 수 비교 -> 큰 수를 맨 뒤에서 두번째까지만 비교 후 보냄(n-1)
# 계속적으로 큰 수를 뒤로 배치함
'''arr = list(map(int, input("Enter the numbers in the list you wanted to sort(seperated by spaces) >> ").split()))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):    # index니까 -1
            if arr[j+1] < arr[j]:
                # arr[j] = arr[j+1]
                # arr[j+1] = arr[j]
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f'{i+1} round {j+1}th sorted arr = {arr}')
            #else, nothing happened
    return arr

print(f'Sorted array = {bubble_sort(arr)}')

'''

# 3. INSERTION SORT
# 기존 리스트 vs. 새로만든 리스트
# 기존리스트 값을 새리스트안에 insert
# when you insert value, compare and sort them
'''
origin_arr = list(map(int, input("enter numbers for the list >> ").split()))

def insertion_sort(origin_arr):
    new_arr = [origin_arr[0]] # create the new list with 1st value of the original list
    for i in range(1, len(origin_arr)):
        j = 0
        while j < i and new_arr[j] < origin_arr[i]: # as long as values are sorted already, j += 1
            j += 1
        # otherwise,
        new_arr.insert(j, origin_arr[i]) # insert origin_arr[i] into new_arr[j] 
        print(f'new arr = {new_arr}')
    return new_arr

print(f'Sorted array = {insertion_sort(origin_arr)}')'''

# 4. INSERTION SORT 2
# 하나의 리스트 안에 두개의 리스트 존재한다고 생각하고 insertion sorting 하는 법
'''
(3, 1, 4, 5, 2) # 정렬이 필요한 기존 리스트
(3) // (1, 4, 5, 2) # 첫번째 항목을 첫번째 리스트(new), 나머지를 두번째 리스트로함(origin)
(1, 3) // (4, 5, 2) # 1을 정렬시킴
(1, 3, 4) // (5, 2) # 4를 정렬시킴
(1, 3, 4, 5) // (2) # 5를 정렬시킴
(1, 2, 3, 4, 5)     # 2를 첫번째 리스트에(new) 정렬시킴
'''
# origin_arr = list(map(int, input("enter numbers for the list >> ").split()))

# def insertion_sort2(arr):
#     for i in range(1, len(arr)):
#         print(f'{i}th new_arr = {arr[:i]} // origin_arr = {arr[i:]}')
#         j = i
#         while 0 < j and arr[j] < arr[j-1]:
#             arr[j], arr[j-1] = arr[j-1], arr[j]
#             j -= 1
#     return arr

# print(f'Sorted arr = {insertion_sort2(origin_arr)}')


# TUPLE
'''multiple inputs assigned multiple variables -> tuple 사용한다고 알려줘야함
toy, gift = 'shoes',  'ps5', 'watch', 'pc' -> Error : expected 2(variables 2개라서)
toy, *gift = 'shoes', 'ps5', 'watch' , 'pc' -> 멀티 인풋 튜플에 넣기 가능('ps5', 'watch' , 'pc'  = gift)'''