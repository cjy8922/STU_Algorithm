#03:20:45.12
import sys
import copy
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
'''
sort쓰면 시간초과!
격자판의 나무가 성장, 번식, 제초제뿌려서 가장 많이 나무 없앨 수 있는 격자판에 뿌려서 없애고, 
제초제의 지속시간 고려해서 없앨 수 있는 나무의 그루 수를 구하는 문제

1. while문으로 박멸이 진행되는 1년을 m년까지 반복하기 위해 과정들은 함수로 구현
2. 나무의 성장 함수
    - 매해 +1되는 나무의 성장 구현하기 위해 격자판에서 나무 있는 곳 grid[i][j] > 0인곳을 찾아서 +1
3. 나무의 번식 함수 => 나무의 번식적용한 grid 리턴
    - 번식할 때 4방향칸 중 빈칸이거나 이미 있는 나무에 더해지므로 grid[i][j] > 0을 찾음
    - 여기서, 제초제의 영향을 안받는 곳이어야 번식 가능하므로 좌표확인할 때 같이 확인
    - 번식 나무 = 현재 나무수 % 가능한 방향칸수 이므로 blank 리스트 만들어 가능한 방향 좌표 저장
        - blank있으면 주위 좌표에 grid[i][j] % len(blank)만큼 번식 구현 가능
4. 제초제의 지속시간을 관리하는 배열 herbicide grid와 같은 크기로 선언해서 관리함
    - 제초제의 지속시간 감소시키는 decrease_herbicide 함수 구현
5. 제초제 뿌려서 없앨 수 있는 나무수가 가장 많은 좌표에 뿌리기 위해 search_trees_to_be_destroyed 함수 구현
    - 대각선방향을 적용하기 위해 dia_x와 dia_y 만들고 k의 범위만큼 적용시키기 위해 for문으로 제어
    - 없앨 수 있는 나무가 같은 경우 행, 열 작은 순서로 우선순위 들어가기 때문에 
        - 좌표를 tx, ty로 저장해 (i, j) < (tx, ty) 확인
    - 없앨 수 있는 나무 수와 좌표 리턴 (max_cnt, tx, ty)
6. 제초제 뿌리고 지속시간 초기화해주는 함수 spray 구현
    - 바로 시간 감소시키기 위해 해당 지속시간 좌표에 c+1
    - 대각선방향으로 제초제 뿌리고 빈칸 0 으로 만들어줌
'''

n, m, k, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

herbicide = [[0] * n for _ in range(n)]  # 제초제 지속시간을 저장하는 배열

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def growth_of_trees(grid): # 나무의 성장 적용한 grid 리턴
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0: # 성장할 나무 있는 곳
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] > 0: # 4방향확인해서 나무 있으면 성장+1
                        grid[i][j] += 1
    return grid

def reproduction_of_trees(grid): # 나무의 번식 적용한 grid 리턴
    new_grid = copy.deepcopy(grid) # 새롭게 카피
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0: # 번식가능한 나무 있는 곳
                blank = [] # 번식할 나무수 계산하기 위해 빈칸 저장
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if grid[nx][ny] == 0 and herbicide[nx][ny] == 0:
                            blank.append((nx, ny))
                if blank:
                    spread = grid[i][j] // len(blank)
                    for x, y in blank:
                        new_grid[x][y] += spread
    return new_grid

# 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래
dia_x = [-1, -1, 1, 1]
dia_y = [-1, 1, -1, 1]
def search_trees_to_be_destroyed(grid, k): # 제초제 뿌렸을 때, 나무가 가장 많이 박멸되는 칸 중 우선순위가 높은 칸 리턴
    max_cnt = -1
    tx, ty = 0, 0
    search_trees = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0:
                cnt_trees_destroyed = grid[i][j]
                for l in range(4):
                    for m in range(1, k + 1):
                        nx = i + dia_x[l] * m
                        ny = j + dia_y[l] * m
                        if 0 <= nx < n and 0 <= ny < n:
                            if grid[nx][ny] <= 0:
                                break
                            if grid[nx][ny] > 0:
                                cnt_trees_destroyed += grid[nx][ny]
                        else:
                            break
                if cnt_trees_destroyed > max_cnt:
                    max_cnt = cnt_trees_destroyed
                    tx, ty = i, j
                elif cnt_trees_destroyed == max_cnt:
                    if (i, j) < (tx, ty):  # 행 우선, 열 우선
                        tx, ty = i, j
    if max_cnt != -1:
        return (max_cnt, tx, ty)
    else:
        return (0, 0, 0)

def spray(x, y):
    grid[x][y] = 0
    herbicide[x][y] = c + 1 #바로 다음턴부터 1씩 감소시키기 위해
    for l in range(4):
        for m in range(1, k + 1):
            nx = x + dia_x[l] * m
            ny = y + dia_y[l] * m
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] == -1:
                    break
                herbicide[nx][ny] = c + 1 # 빈칸이어도 제초제 영향있으니까
                if grid[nx][ny] > 0: # 표시하고 break
                    grid[nx][ny] = 0
                elif grid[nx][ny] == 0:
                    break  # 0이면 제초제 뿌리고 종료
            else:
                break        

def decrease_herbicide(): # 매해 제초제 지속시간 감소
    for i in range(n):
        for j in range(n):
            if herbicide[i][j] > 0:
                herbicide[i][j] -= 1

cnt, year = 0, 0
while year < m:
    growth_of_trees(grid)
    grid = reproduction_of_trees(grid)
    cnt_trees_destroyed, x, y = search_trees_to_be_destroyed(grid, k)
    cnt += cnt_trees_destroyed
    spray(x, y)
    decrease_herbicide()
    year += 1 
print(cnt)