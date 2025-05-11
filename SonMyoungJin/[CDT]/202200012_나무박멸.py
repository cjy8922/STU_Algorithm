#03:20:45.12
import sys
import copy
from collections import deque

def input():
    return sys.stdin.readline().rstrip()
'''
sort쓰면 시간초과!

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