'''
유저 인풋으로 소수(prime number) 구하기
💡 소수는 1과 자기 자신을 제외한 어떤 수로도 나누어 지지 않는다
'''
# [01] 소수 확인하기기
# print("Enter any number >>")
# user_nums = int(input())

# def is_prime(n) :
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         else:
#             return True

# if is_prime(user_nums):
#     print(user_nums, "/ its a prime number")
# else:
#     print(user_nums, "/ its not a prime number")
    
# [02] 2 부터 N 까지 몇개의 소수가 있는지 확인하는 프로그램
# def is_prime(n) :
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#         else:
#             return True

# print("Enter a number to check how many prime numbers exist >>")
# user_nums2 = int(input())
# count = 0

# for i in range(2, user_nums2):
#     if is_prime(i):
#         count += 1

# #print("There are ", count, " of prime nums are existed from 2 to", user_nums2)
# print(f'2부터 {user_nums2} 까지 소수는 총 {count}개 있습니다.')

# [03] Check prime numbers from big nums something like 40000
# 소수 구하는 알고리즘 속도 줄이기
'''
책 본문 원리 설명 발췌
40000이라는 숫자가 소수인지 체크하기 위해서 39999까지 체크하는 것이 아니라
400까지만 체크해도 나머지 100은 이미 체크가 된 것이고, 
250까지만 체크해도 160까지는 이미 체크된 것이라 더 이상 안 해도 된다는 뜻입니다.
40000은 정사각형의 크기가 되는 200까지만 체크하면 
더 이상 소수인지 아닌지 체크하지 않아도 된다는 뜻이 됩니다. 
'''
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
        return True

print("Enter a big number to test something like 40000 >>")
user_input3 = int(input())
counts = 0

for i in range(2, user_input3):
    if is_prime(i):
        counts += 1
print(f"2 부터 {user_input3} 까지의 prime number 갯수는 {counts} 개 입니다")