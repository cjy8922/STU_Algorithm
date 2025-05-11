#00:37:40.49
import sys

sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
N일 동안 매일의 방문자 수 주어질 때, 길이 X인 구간 중, 가장 많은 방문자 수 합과 그 구간의 갯수 구하는 문제
- sum(DAU[i : i + X]) 이렇게 풀면 매번 X개의 합을 구해야해서 O(N*X)
- 따라서, 이전 구간의 합을 이용해서 다음 구간의 합을 O(1)시간에 계산할 수 있는 슬라이딩 윈도우 기법 사용.
- cur_sum += DAU[i] - DAU[i - X] : 새로운 오른쪽 값 하나 더하고, 왼쪽 끝 값을 하나 빼는 식
 => 매 이동마다 +,- 계산만 하기 떄문에 O(N)에 모든 구간 확인 가능
 
1. 윈도우 크기(X) 고정되어있고, 초기 윈도우 합 저장하기 위해 cur_sum = sum(DAU[:X])
2. 슬라이딩 윈도우하기 위해서 for문으로 X<= i < N범위에서 cur_sum += DAU[i] - DAU[i - X] 계산
3. 초기 윈도우가 최대값일 수 있으니까 cnt = 1 로 초기화
    - 더 큰 최댓값만나면 다시 cnt = 1로 초기화
'''

N, X = map(int, input().split())
DAU = list(map(int, input().split()))

# 초기 윈도우 합
cur_sum = sum(DAU[:X])
max_AU = cur_sum
cnt = 1 # 초기 윈도우가 최대일수있으니까 1로 초기화
for i in range(X, N):
    # 슬라이딩 윈도우 : 이전 합에서 앞 값을 빼고 새 값 더함.
    cur_sum += DAU[i] - DAU[i - X]
    if cur_sum > max_AU:
        max_AU = cur_sum
        cnt = 1 # 새로운 최대값이므로 카운트 새로 시작
    elif cur_sum == max_AU:
        cnt += 1 # 최댓값과 같으면 +1

if max_AU == 0:
    print('SAD')
else:
    print(max_AU)
    print(cnt)