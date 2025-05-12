# 00:58:15.54
import sys
from collections import defaultdict

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()
'''
문자열 W에서 어떤 문자를 K개 포함하는 가장 짧은 연속문자열의 길이와 가장 긴 연속문자열 길이구하는 문제
(양쪽 끝 문자열이 같아야함 길거나 짧거나)
- 연속문자열의 길이와 어떤 문자의 갯수를 모두 구하기위해 각 문자의 인덱스를 기록해서 풀어야함.
1. 각 문자의 인덱스를 모두 기록하기 위해 defaultdict(list)로 빈리스트 자동으로 생성해서 딕셔너리 초기화
    - 각 문자의 인덱스 append
2. 한 문자가 K번 등장하는 문자열 찾기위해 index_dict.values()에서 각 문자의 인덱스 뽑아서 거리 계산
    ex) (abaaaba, K=3), index_dict['a'] = [0,2,3,4,6]
        length = pos[i+3-1] - pos[i] + 1 => K개 만큼 포함시켰을 때 길이구해서 짧은 거, 긴 거 구함.
'''
T = int(input())

for _ in range(T):
    W = input()
    K = int(input())
    index_dict = defaultdict(list)
    # 각 문자의 인덱스 기록
    for idx, ch in enumerate(W):
        index_dict[ch].append(idx)
    
    min_len = 1e4 + 1
    max_len = -1
    # 각 문자마다 K개씩 연속된 인덱스 뽑아서 거리 계산
    for pos in index_dict.values():
        if len(pos) < K: # 문자열 등장 횟수가 부족하면 패스
            continue
        for i in range(len(pos) - K + 1):
            length = pos[i + K - 1] - pos[i] + 1
            min_len = min(min_len, length)
            max_len = max(max_len, length)

    if min_len == 1e4 + 1:
        print(-1) 
    else:
        print(min_len, max_len)

# 시간 초과!
# for i in range(K-1, len(W)):
#     for j in range(len(W) - i):
#         if W[j] == W[j+i] and  W[j:j+i+1].count(W[j]) == K:
#             #print(W[j:j+i+1], i+1)
#             len_str.append(i+1)