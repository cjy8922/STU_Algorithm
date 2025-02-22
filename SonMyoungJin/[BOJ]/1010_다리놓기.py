#00:15:39.72
#00:34:47.10
import sys
import math

#sys.stdin = open('input.txt', 'r')

'''
N개 사이트만큼 M개 사이트를 연결해 다리를 놓는 문제 (0< N <= M <30)
1. M개에서 N개를 뽑는 경우의 수 구하는 문제 => 조합
    - math.comb(M, N) 사용해도 풀림.
    - 조합 식 = M! / (N! * (M-N)!)
2. 서쪽 사이트와 동쪽 사이트간의 연결이 가능한 경우의 수를 점차적으로 계산 => DP를 사용해서 풀 수 있음.
    - dp[i][j] : 서쪽 i개의 사이트와 동쪽 j개의 사이트를 연결하는 경우의 수 저장.
    - dp[0][j] = 1 (아무것도 연결 안함), dp[i][0] = 0 (연결할 게 없음)
    - dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
'''

def input():
    return sys.stdin.readline().rstrip()

def combination(M, N):
    if N == 0 or M == 0:
        if N == 0 and M != 0:
            return 0
        else:
            return 1
    
    result_M = 1
    result_N = 1
    num = M
    
    while num > (M - N):
        result_M *= num
        num -= 1
    
    for i in range(1, N+1):
        result_N *= i
           
    return result_M // result_N
        
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(combination(M, N))
    #print(math.comb(M, N))
    
    
'''
# DP
# 부분 문제로 나누어 해결
# dp[i][j] : 서쪽 i개의 사이트와 동쪽 j개의 사이트를 연결하는 경우의 수 저장.
    - dp[0][j] = 1 (아무것도 연결 안함), dp[i][0] = 0 (연결할 게 없음)
    - dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
        1. i번째 사이트와 j번째 사이트를 연결하는 경우
            - i번째와 j번째 연결한다면, 남은 문제는 i-1개 사이트와 j-1개 사이트 연결하는 문제, dp[i-1][j-1]만큼의 방법이 있음.
        2. i번째 사이트와 j번째 사이트를 연결하지않는 경우
            - i번째에 j번째 연결 안한다면, 남은 문제는 i개 사이트에 j-1개 사이트 연결하는 문제, dp[i][j-1]만큼의 방법이 있음.

def combination(M, N):
    #dp 테이블
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    # 초기 조건 설정
    for j in range(M+1):
        dp[0][j] = 1 #서쪽 사이트 0개에서 동쪽 사이트 j개에 연결하는 방법 1가지 (j개에서 0개 뽑는 방법)
    
    # DP 점화식에 따라 테이블을 채워 나감
    for i in range(1, N + 1):
        for j in range(j, M + 1): #조합이니까 j >= i
            # 서쪽 i-1개 사이트, 동쪽 j-1개 사이트와 연결하고
            dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
    
    return dp[N][M]

'''