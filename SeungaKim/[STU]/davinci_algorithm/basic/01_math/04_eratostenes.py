'''
소수를 구하기 위해서 하나하나 소수인지 아닌지 판단했습니다. 
하지만 소수를 미리 다 찾아두는 것이 더 편할 때가 있습니다. 
가령 200에서 300 사이의 소수의 개수를 구하고, 
또 200에서 500 사이의 소수의 개수를 구해야 한다면 
200에서 300 사이의 소수의 개수는 이미 구했기 때문에 또다시 계산할 필요가 없습니다.

어떤 수가 소수인지 알고 싶을 때는 앞에서 배운 방법을 사용하고,
주어진 범위내에서 소수를 찾을 때 이 방법을 사용합니다. 
이렇게 대량의 소수를 빠르게 찾을 때 사용하는 알고리즘이 에라토스테네스의 체라는 것입니
'''
# 소수(prime nums) 들의 배수 != prime nums
# [01] 1 ~ 50 까지 사이 수에서 몇개의 소수가 존재하는가?
# 풀이 참고함***

# print("Enter a number to check nums of prime >> ")
# nums = int(input())
# count_prime = 0
# prime_list = (nums + 1) * [True]     # initialized them as True

# prime_list[0], prime_list[1] = False, False # 0 과 1 소수 x -> 제거

# for i in range(2, nums + 1) :
#     if prime_list[i] :               # ***** 이부분 해결ㄴ. 몰랐음
#         for j in range(2*i, nums +1, i) :
#             '''
#             range(start, stop, step),

#             - start: 어디서부터 시작할지
#             - stop: 어디까지 갈지 
#             - step: 몇 칸씩 증가할지
            
#             (i.e) 4, 6, 8.. n+1 까지 (i=2 일때)
#                     6, 9, 12 (i = 3 일때)
#             '''
#             prime_list[j] = False

# # counting prime nums
# for i in range(2, nums + 1):
#     if prime_list[i]:
#         count_prime += 1

# print(f"2 와 {nums} 사이 소수의 갯수는 {count_prime} 입니다.")

## 에라토스테네스의 채(2960)
'''
문제
에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.

이 알고리즘은 다음과 같다.

2부터 N까지 모든 정수를 적는다.
아직 지우지 않은 수 중 가장 작은 수를 찾는다. 
이것을 P라고 하고, 이 수는 소수이다.
P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 K가 주어진다. (1 ≤ K < N, max(1, K) < N ≤ 1000)

출력
첫째 줄에 K번째 지워진 수를 출력한다.

예제 입력 1 
7 3
예제 출력 1 
6
'''
user_intput_N, user_input_K = map(int, input().split())
prime_list = (user_intput_N + 1)*[True]
prime_list[0], prime_list[1] = False, False
count_k = 0

for i in range(2, user_intput_N+1):
    if prime_list[i] :
        for p in range(i, user_intput_N+1, i):  # *****  바보야야.. p 부터 지우라고 문제에 적혀있는뎁쇼. 2*i 아니고 i 도 포함해야지
            if prime_list[p] == False:  # *****
                continue                # *****
            prime_list[p] = False
            count_k += 1
            if count_k == user_input_K:
                print(p)
