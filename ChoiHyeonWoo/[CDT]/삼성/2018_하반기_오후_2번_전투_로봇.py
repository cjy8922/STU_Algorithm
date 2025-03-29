import sys
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
level = 2
check_level = 0
cnt = 0
def is_Finished():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and board[i][j] < level:
                return False
    return True 
def find_robot():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                return i, j

def kill_monster(robot_x, robot_y):
    global level, cnt, check_level
    Q = deque()
    Q.append((robot_x, robot_y))
    visited = [[-1] * n for _ in range(n)]
    visited[robot_x][robot_y] = 0
    check = []
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] <= level and visited[nx][ny] == -1:
                Q.append((nx, ny))
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                if board[nx][ny] > 0 and board[nx][ny] < level:
                    check.append((visited[nx][ny], nx, ny))
    if check:
        check.sort(key = lambda x: (x[0], x[1], x[2]))
        check_level += 1
        if check_level == level:
            level += 1
            check_level = 0
        return check[0][0], check[0][1], check[0][2]
    return -1, -1, -1

while 1:
    if is_Finished() == True:
        break
    robot_x, robot_y = find_robot()
    count, n_x, n_y = kill_monster(robot_x, robot_y)
    if count != -1:
        cnt += count
        board[robot_x][robot_y] = 0
        board[n_x][n_y] = 9
    else:
        break
print(cnt)