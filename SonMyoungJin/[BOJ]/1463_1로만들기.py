#00:34:01.25
import sys

#sys.stdin = open("input.txt", 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
N을 1로 만드는 최소 연산 횟수 구하는 문제(3,2로 나누거나 1빼거나)
N = 1이면 최소 연산 횟수 0
N = 2 or 3이면 최소 연산 횟수 1
N = 4이면, 4%2 == 0이니까 2로 나눌수 있고, 연산횟수 +1
    그러면 2에 대한 최소 연산 횟수 1이니까 1+1로 2가 답.
    => 이전 연산 2,3 등의 최소 연산 횟수를 저장해서 참고해 4이상의 큰 수에 대한 최소 연산 횟수을 구해야함
    => dp[i]를 선언해 i를 1로만드는 최소 연산 횟수를 저장함
'''

N = int(input()) # 1 <= N < 1e6
#dp[i]: i를 1로 만드는 최소연산횟수
#dp[0]은 0, dp[1] == 0, dp[2],dp[3] == 1 
dp = [0, 0, 1, 1] + [0] * (N-3)

for i in range(4, N+1):
    tmp3, tmp2, tmp1 = 1e7, 1e7, 1e7
    # 2와 3으로 나누어지는지 모두 확인
    if i % 3 == 0:
        tmp3 = dp[i//3] + 1
    if i % 2 == 0:
        tmp2 = dp[i//2] + 1
    tmp1 = dp[i-1] + 1 # 1로는 무조건 뺄 수 있으니까
    #세 연산중 가장 최소로
    dp[i] = min(tmp3, tmp2, tmp1)

print(dp[N])