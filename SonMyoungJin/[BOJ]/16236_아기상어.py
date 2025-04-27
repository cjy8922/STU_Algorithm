#01:14:17.96
import sys
from collections import deque

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
아기상어가 잡아먹을 수 있는(본인보다 크기 작은) 물고기 모두 잡아먹는 문제
- 아기상어의 크기는 먹은 물고기 수에 따라 달라지기 떄문에
    - 상어 크기는 size_bs에, 먹은 물고기수는 eat 변수에 저장

- 물고기 한마리 먹을때마다 상어 위치와 크기, 먹을 수 있는 물고기가 달라지므로 1마리 먹을 때마다 과정 반복
1. 아기 상어는 상하좌우로 확인해 먹을 수 있는 물고기가 있으면 이동해서 먹고, 없으면 멈추니까
    - bfs로 사용해 먹을 수 있는 모든 물고기 탐색하는 함수 정의
        - 없으면 종료
        - 1마리 이상이면 정렬해서 가장 우선순위 높은 물고기 선택해서 리턴
        - 거리 업데이트하기위해 2차원 배열 visited 사용
2. 상어 이동, 먹기
3. 크기 증가 여부 확인 
'''

N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9: #처음 아기 상어의 위치
            sx, sy = i, j
            space[i][j] = 0 # 상어 위치 빈칸으로 바꿔줌

size_bs, eat, time = 2, 0, 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, size_bs): # 현재 상어 위치에서 먹을 수 있는 모든 물고기 탐색
    queue = deque([(sx, sy)])
    visited = [[-1] * N for _ in range(N)]
    visited[sx][sy] = 0
    fishes = [] # 먹을 수 있는 물고기들 
    while queue:
        cx, cy = queue.popleft()
        space[cx][cy] == 0 # 현재 상어위치
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if space[nx][ny] <= size_bs and visited[nx][ny] == -1: # 방문가능
                    visited[nx][ny] = visited[cx][cy] + 1 # 상어의 이동거리 업데이트
                    queue.append((nx, ny))
                    if 0 < space[nx][ny] < size_bs: # 먹을 수 있는 크기의 물고기이면
                        fishes.append((visited[nx][ny], nx, ny))
    
    # 거리, 위, 왼쪽순으로 정렬
    fishes.sort()
    if fishes:
        return fishes[0] # 가장 우선순위 높은 물고기
    else: # 먹을수있는 물고기 없으면 None
        return None
    
while True: # 물고기 하나 먹을때마다 실행
    result = bfs(sx, sy, size_bs) 
    if result is None: #먹을수있는 물고기 없으면
        break
    dist, fx, fy = result
    time += dist # 이동시간 == 이동거리 * 1초
    eat += 1     
    space[fx][fy] = 0
    sx, sy = fx, fy
    if eat == size_bs:
        size_bs += 1
        eat = 0
        
print(time)