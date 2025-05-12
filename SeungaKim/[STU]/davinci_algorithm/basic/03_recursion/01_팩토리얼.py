'''
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

출력
첫째 줄에 N!을 출력한다.
'''
# 6:54
# n = int(input())

# # out of range
# if n < 0 or n > 12:
#     exit()
# else:
#     multiply = 1
#     while n - 1 :
#         multiply *= n
#         n -= 1
#     print(multiply)
        

# 7:02 
# 아? 0 인 케이스 고려 안함; 시간초과 뜸

# else:
#     multiply = 1
#     for i in range(1, n+1):
#         multiply *= i

# print(multiply)



# recursion
N = int(input())
if N < 0 or N > 13:
    exit()
    
def recursive_func(n):
    # 종료 조건
    if n < 1:
        return 1
    return n * recursive_func(n-1)

print(recursive_func(N))

# 7:16