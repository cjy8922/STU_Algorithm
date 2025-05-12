#01:43:00.54
import sys
from collections import defaultdict

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
코드참고
k개의 초밥 접시 연속해서 먹고 쿠폰 초밥도 합쳐서 먹을 수 있는 최대 초밥 종류수 구하는 문제
- 초밥의 종류 수를 구하기 위해 슬라이싱한 초밥 리스트를 set으로 만들어 구하면 O(N*k)로 시간초과남
- k개씩 접근할 때 앞에 빼고 뒤에 추가하는 슬라이싱 윈도우 사용하면
    - 초기화 O(k) + 슬라이딩 O(N)으로 통과 가능
1. 기본적으로 k개씩 접근
    - k개 안에서 초밥종류와 빈도수 세기 위해 type_of_sushi int변수와 sushi_cnt 딕셔너리 선언
    - for문으로 0부터 k까지 딕셔너리와 종류수 초기화
    - 최대 종류수 max_types는 현재 k개에서 쿠폰 초밥없으면 +1
2. 현재 sushi_cnt와 type_of_sushi상태에서 앞의 초밥빼고 뒤의 초밥 더해서 total_types를 구함
    - total_types 중 max를 구함
'''

N, d, k, c = map(int, input().split())
sushi_belt = [int(input()) for _ in range(N)]

sushi_cnt = defaultdict(int) # 초밥 빈도수 딕셔너리
type_of_sushi = 0 # 초밥 종류 수
# 초기화
for i in range(k): # sushi_belt 리스트 0 ~ k-1로 일단 초기화
    if sushi_cnt[sushi_belt[i]] == 0:
        type_of_sushi += 1
    sushi_cnt[sushi_belt[i]] += 1

if sushi_cnt[c] == 0:
    max_types = type_of_sushi + 1
else:
    max_types = type_of_sushi

# 슬라이딩 윈도우
for i in range(1, N):
    # 앞의 초밥 제거
    prev = sushi_belt[i - 1]
    sushi_cnt[prev] -= 1
    if sushi_cnt[prev] == 0:
        type_of_sushi -= 1
        
    # 뒤의 새로운 초밥 추가
    next = sushi_belt[(i + k - 1) % N]
    if sushi_cnt[next] == 0:
        type_of_sushi += 1
    sushi_cnt[next] += 1
    
    if sushi_cnt[c] == 0:
        total_types = type_of_sushi + 1
    else:
        total_types = type_of_sushi
    
    max_types = max(max_types, total_types)
print(max_types)

# 시간 초과!
# 
# for first in range(N):
#     # 회전
#     if first <= (N - k):
#         last = first + k
#         eat = set(sushi_belt[first : last])
#     else:
#         last = k - (N - first)
#         eat = set(sushi_belt[first:] + sushi_belt[:last])

#     if c not in eat:
#         if max_cnt <= len(eat):
#             max_cnt = len(eat) + 1
#     else: # c in eat:
#         if max_cnt <= len(eat):
#             max_cnt = len(eat)
        
# print(max_cnt)   
