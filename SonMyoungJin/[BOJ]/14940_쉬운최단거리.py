#00:50:18.08
import sys
from collections import deque

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
목표지점에서 각 지점까지의 최단거리를 출력하는 문제
1. 현재지점까지의 최단거리 = 목표 지점부터 현재 지점 바로 전까지의 최단거리+ 바로전에서 현재지점까지의 최단거리(아마 1)
    - 각 지점에서의 최단거리들을 저장해서 꺼내서 사용해야함 2차원 배열 table을 지도 grid와 같은 크기로 선언해서 최단거리 저장
2. 2(목표지점)에서 BFS 시작
    - 1인곳은 방문가능 (체크하면서 table에 거리저장)
    - 0인곳은 방문불가
3. 1이여서 방문이 가능하지만 막혀있거나 해서 도달하지 못한경우 -1 출력

'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# table[i][j] : (i,j)에서 목표지점까지의 최단거리, -1로 초기화
table = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            tx, ty = i, j
            table[i][j] = 0

queue = deque([(tx, ty, table[tx][ty])])
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
while queue:
    cx, cy, cd = queue.popleft()
    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 1 and table[nx][ny] == -1:
                table[nx][ny] = cd + 1
                queue.append([nx, ny, table[nx][ny]])
            
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(0, end=' ')
        elif table[i][j] == -1: # 갈 수 있는 땅인데 목표점까지 도달 불가능 => -1
            print(-1, end=' ')
        else:
            print(table[i][j], end=' ')
    print()