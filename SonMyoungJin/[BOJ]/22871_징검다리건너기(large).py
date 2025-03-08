#02:00:00.00
import sys

#sys.stdin = open('input.txt', 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드 참고 : https://www.acmicpc.net/source/84491926

N개의 돌 나열되어 있을 때, 돌 A[0] -> A[N-1]으로 건너가는 모든 경우 중 힘 K의 최솟값 구하는 문제
    - i번째 돌 -> j번째 돌 건너는 힘 => (j-i)*(1+abs(A[i] - A[j]))
- 2 <= N <= 5000
- 1 <= A[i] <= int(1e6)

1. 각 돌에 도달하기 위해 이전에 계산된 값들을 기반으로 최적의 값을 구해야하므로 DP 사용.
    - 반복적으로 계산되는 부분을 저장하여 중복을 피함.
    
2. 1번째 돌에서 출발하여 i번째 돌에 도달할 때 드는 최대 힘이 최소가 되도록 계산하기 위해 dp 배열 선언하여 값을 저장.
    - dp[i] : i번째 돌에 도달할 때의 최소 최대 힘
    
3. i번째 돌에 도달할 때의 최소 최대힘 dp[i]를 구하기 위해 모든 이전 돌 j를 고려.
    - 각 j에 대해, i번째 돌로 이동할 때 드는 힘을 계산하고, 그 중 최대 힘을 dp[j]값과 비교하여 최소화
    => dp[i] = min(dp[i], max((i - j) * (1 + |A[i] - A[j]|)))


    i = 1, 2번째 돌까지 도달 K값
        - j = 0 (1번째 -> 2번째)
            - dp[1] = min(dp[1], 4)
                => 4
    i = 2, 3번째 돌까지 도달 K값
        - j = 0 (1번째 -> 3번째)
            - (2 - 0) * (1 + |1 - 1|) = 2 
            - dp[2] = min(dp[2], 2)
                    => 2
        - j = 1 (2번째 -> 3번째)
            - (2 - 1) * (1 + |1 - 4|) = 4
            -  dp[2] = min(dp[2], 4)
                    => 2
'''

N = int(input())
A = list(map(int, input().split()))

# 가능한 최대 K값 계산 
# 최악의 경우 : A[0] -> A[N-1] 바로 건너는 경우, A[0] - A[N-1] == 1e6 인 경우
# K == (j-i) * (1 + abs(A[i] - A[j]))
Max_K = (N - 1) * int(1e6)

# dp[i] : i번째 돌에 도달할 때 필요한 최소의 최대 K값(== A[0]에서 A[N-1]까지 가는 최대 K값)
# dp[0] : 1번째 돌은 이동할 필요없으니까 0
dp = [0] + [Max_K] * (N - 1)

# i번째 돌에 도달
for i in range(1, N): # 두번째 돌부터 N번째까지
    # i번째 돌에 도달하기 위해, 0부터 i-1까지 체크 (이전 돌 중 어떤 돌에서 출발해야 최소값일까)
    for j in range(i): 
        # j -> i까지 도달에 필요한 힘과 j까지 도달한 힘(dp[j])중 더 큰 게 K값
        # => i까지 도달하는 데 최대 힘
        k = max((i - j) * (1 + abs(A[i] - A[j])), dp[j])
        
        # i번째 돌에 도달하는 데 드는 최소 K값 갱신
        dp[i] = min(dp[i], k)

print(dp[-1])


'''
pypy3만 통과!

- 최소 K값 구해야 함.
    == K값이 주어졌을 때, 마지막 돌까지 갈 수 있는가? 라는 결정 문제 => 이분 탐색
- i번째 돌에 도달할 수 있는지 확인 필요.
    == i번째 돌에 도달 가능 여부(힘이 K이하이면 도달 가능으로) 계산하기 위해 K_table 배열 선언해 사용 => DP


N = int(input())
A = list(map(int, input().split()))

def cross_stepping_stone(K, N, A):
    # i-1번째 돌 도달 가능 여부
    K_table = [False] * N
    K_table[0] = True # 1번째 돌에서 시작
     
    for i in range(N):
        if not K_table[i]:
            continue
        
        for j in range(i + 1, N):
            # 필요한 힘만 계산
            power = (j-i) * (1 + abs(A[i] - A[j]))
            
            if power <= K:
                K_table[j] = True # 도달 가능한 돌 모두 표시
            
    return K_table[N-1] # 마지막 돌에 도달 가능 여부

def binary_search(N, A):
    # 가능한 최소 K값은 0
    left = 0
    # 가능한 최대 K값 계산 (최악의 경우 : A[0] -> A[N-1] 바로 건너는 경우)
    right = (N - 1) * (1 + abs(A[0] - A[-1]))
    
    # 이분 탐색으로 K의 최솟값 찾기
    answer = right
    while left <= right:
        mid = (left + right) // 2
        if cross_stepping_stone(mid, N, A):
            answer = mid
            right = mid - 1  # 더 작은 K를 찾아보자
        else:
            left = mid + 1  # 더 큰 K가 필요함
    
    return answer

print(binary_search(N,A))
'''