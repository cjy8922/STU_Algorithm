#01:07:24.05
import sys
from collections import deque

#sys.stdin = open("input.txt", 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
로봇청소기의 작동 방식을 그대로 구현하는 문제
1. (현재 위치, 방향)을 저장하고 다음 상태를 결정하기 위해 큐를 선언해 큐에 추가
    - 그냥 while 루프방식이 직접 업데이트하면서 진행할 수 있어 더 간단함
'''

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 로봇청소기 있는 칸(r, c), 바라보는 방향 d
queue = deque([(r, c, d)])
cleaned = 0
# 북쪽 : 상, 동쪽: 우, 남쪽: 하, 서쪽: 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while queue:
    cur_r, cur_c, cur_d = queue.popleft()
    # 1. 현재 칸이 청소되지 않았으면 청소
    if room[cur_r][cur_c] == 0:
        cleaned += 1
        room[cur_r][cur_c] = 2 # 청소한 칸은 2로 표시
        
    # 주변 4칸 중 청소되지 않은 빈 칸이 있는지 확인
    unclean = False
    for i in range(4):
        next_r = cur_r + dx[i]
        next_c = cur_c + dy[i]
        if 0 <= next_r < N and 0 <= next_c < M and room[next_r][next_c] == 0:
            unclean = True
            break

    if unclean: #청소되지 않은 빈 칸이 있으면
        # 2. 반시계 방향으로 90도 회전
        next_d = (cur_d + 3) % 4
        
        # 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        next_r = cur_r + dx[next_d]
        next_c = cur_c + dy[next_d]
        if 0 <= next_r < N and 0 <= next_c < M and room[next_r][next_c] == 0:
            queue.append((next_r, next_c, next_d))
        else:
            # 앞쪽 칸이 청소할 수 없으면 회전만 하고 다시 현위치 검사
            queue.append((cur_r, cur_c, next_d))
            
    else: # 청소되지 않은 빈 칸이 없으면
        # 후진
        next_r = cur_r - dx[cur_d]
        next_c = cur_c - dy[cur_d]
        # 후진 가능하면 후진
        if 0 <= next_r < N and 0 <= next_c < M and room[next_r][next_c] != 1:
            queue.append((next_r, next_c, cur_d))
        # 후진 못하면 작동 멈춤 (큐에 추가하지 않음)

print(cleaned)
                        
