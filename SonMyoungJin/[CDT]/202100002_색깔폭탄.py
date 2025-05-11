import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

'''
가장 우선순위가 큰 폭탄을 찾아서 제거하고, 중력영향받고, 돌리고해서 점수계산하는 문제
1. 가장 크기 큰 폭탄 묶음을 찾아서 우선순위가 높은 폭탄 묶음을 1개 리턴 => bfs_bomb(grid)
    - 같은색깔이나 빨간색인 폭탄을 상하좌우로 찾아 묶어야하기 때문에 BFS
    - 빨간색이 아닌 색을 기준으로 우선순위 정해야하기 때문에 폭탄은 빨간색폭탄과 빨간색 아닌 폭탄으로 따로 묶어놓음
2. 폭탄을 삭제하기 위한 함수 => del_bomb
    - 폭탄을 삭제한 빈공간을 표현하기 위해 -2를 대입
    - 삭제하는 순간 점수를 계산하기 떄문에 score에 점수를 계산해 리턴
3. 중력의 영향을 구현하기 위한 함수 => gravity
    - 각 열은 고정해놓고 밑에서 두번째(행)부터 확인하여 밑에서 첫번째행이 빈공간이면 거기로
    - 돌이면 -1 안떨어짐
4. 반시계방향으로 90도 돌리기 위한 함수 => rotate
    - 시계방향 90도 : (i, j) -> (j, n-i-1)
    - 시계방향 180도 : (i, j) -> (n-i-1, n-j-1)
    - 시계방향 270도 : (i, j) -> (n-j-1, i)
'''

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs_bomb(grid): # 가장 크기가 큰 폭탄 묶음찾아 우선순위 높은 폭탄 묶음1개 리턴
    visited = [[False] * n for _ in range(n)]
    bombs = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0 and not visited[i][j]: # 빨간색이나 돌이아닌 폭탄일 때 묶음 가능
                queue = deque([(i, j)])
                bomb = [(i,j)] # 빨간색 아닌 폭탄 묶음 저장할 변수
                visited_red = [] # 빨간색 폭탄 따로 저장하기 위한 배열 (우선순위에 따라 정렬해야하므로)
                visited[i][j] = True
                red = 0 # 빨간색 폭탄 갯수
                size = 1 # 폭탄 묶음 크기
                while queue:
                    cx, cy = queue.popleft()
                    for k in range(4):
                        nx = cx + dx[k]
                        ny = cy + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if grid[nx][ny] == grid[i][j] or grid[nx][ny] == 0: # 같은 색깔이거나 빨간색이면
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                                size += 1
                                if grid[nx][ny] == 0: # 근데 빨간색인 경우
                                    visited_red.append((nx, ny))
                                    red += 1
                                else: # 같은 색깔인 경우
                                    bomb.append((nx, ny))
                if visited_red:
                    for x, y in visited_red:
                        visited[x][y] = False # 빨간색은 다른 묶음에 들어갈 수도 있으니까 재방문 가능
                if size >= 2 and (size - red) >= 1 and bomb: # 폭탄이 2개이상, 빨간색 아닌 색깔이 1개이상 있어야 정상 폭탄묶음
                    bomb.sort(key = lambda x: (-x[0], x[1])) # 기준점찾기 위해 행 가장크고 열 가장 작은 순으로 정렬
                    #print(bomb, visited_red)
                    bombs.append((size, red, bomb[0][0], bomb[0][1], bomb, visited_red))
    if bombs:
        bombs.sort(key = lambda x: (-x[0], x[1], -x[2], x[3]))
        #print(bombs[0])
        return bombs[0]
    else:
        return None

def del_bomb(bomb_found, grid): # 폭탄묶음을 삭제
    score = 0
    bomb_size, red, x, y, rest_bomb, red_bomb = bomb_found
    for i, j in rest_bomb:
        grid[i][j] = -2 # 삭제해서 빈공간이라는 표시로 -2
    for i, j in red_bomb:
        grid[i][j] = -2
    score += bomb_size * bomb_size
    return score
    #print(grid)

def gravity(grid): # 중력 작용
    for j in range(n): # 열은 고정
        for i in range(n - 2, -1, -1): # 아래에서 두번째부터 떨어질 공간있으니까
            if grid[i][j] >= 0: # 폭탄이면
                row = i
                while True:
                    if 0 <= row+1 < n and grid[row+1][j] == -2: # 현재 행보다 아래가 빈 공간이면
                        grid[row+1][j], grid[row][j] = grid[row][j], grid[row+1][j]
                        row += 1
                    else: 
                        break

def rotate(grid): # 반시계방향으로 90도 회전
    new_grid = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[n - j - 1][i] = grid[i][j]
    return new_grid

total_score = 0
while True:
    bomb_found = bfs_bomb(grid)
    if bomb_found:
        total_score += del_bomb(bomb_found, grid)
    else:
        break
    gravity(grid)
    grid = rotate(grid)
    gravity(grid)

print(total_score)
