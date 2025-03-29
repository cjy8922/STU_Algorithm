import sys
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
input = sys.stdin.readline
n, m, battery = map(int, input().split())
board = [[[] for _ in range(n)]for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j in range(n):
        #-999은 벽
        if a[j] == 1: a[j] = -999
        board[i][j].append(a[j])
x, y = map(int, input().split())
#-1000은 자동차
board[x-1][y-1].append(-1000)
board[x-1][y-1].sort(reverse=True)
for i in range(1, m + 1):
    x_s, y_s, x_e, y_e = map(int, input().split())
    if 0 in board[x_s-1][y_s-1]:
        board[x_s-1][y_s-1].remove(0)
    if 0 in board[x_e-1][y_e-1]:
        board[x_e-1][y_e-1].remove(0)
    board[x_s-1][y_s-1].append(i)
    board[x_s-1][y_s-1].sort(reverse=True)
    board[x_e-1][y_e-1].append(-i)
    board[x_e-1][y_e-1].sort(reverse=True)

def is_Finished():
    global sign
    if battery < 0:
        sign = 1
        return True
    for i in range(n):
        for j in range(n):
            if board[i][j] and board[i][j][0] > 0:
                return False
    return True
    
def find_car():
    for i in range(n):
        for j in range(n):
            if board[i][j] and board[i][j][-1] == -1000:
                board[i][j].pop()
                return i, j

def find_passenger(car_x, car_y):
    global battery
    Q = deque()
    Q.append((car_x, car_y))
    visited = [[-1] * n for _ in range(n)]
    visited[car_x][car_y] = 0
    check = []
    # print(board[car_x][car_y])
    if board[car_x][car_y] and board[car_x][car_y][0] > 0:
        return car_x, car_y
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if board[nx][ny] and board[nx][ny][-1] == -999:
                    continue
                Q.append((nx, ny))
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                if board[nx][ny] and board[nx][ny][0] > 0:
                    check.append((visited[nx][ny], nx, ny))
    if check:
        check.sort(key = lambda x : (x[0], x[1], x[2]))
        battery -= check[0][0]
        return check[0][1], check[0][2]
    return -1, -1

def move_passenger(passenger_x, passenger_y):
    global battery, sign
    passenger = board[passenger_x][passenger_y].pop(0)
    Q = deque()
    Q.append((passenger_x, passenger_y))
    visited = [[-1] * n for _ in range(n)]
    visited[passenger_x][passenger_y] = 0
    while Q:
        temp = Q.popleft()
        for k in range(4):
            nx = temp[0] + dx[k]
            ny = temp[1] + dy[k]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if board[nx][ny] and board[nx][ny][-1] == -999:
                    continue
                Q.append((nx, ny))
                visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                if board[nx][ny] and -passenger in board[nx][ny]:
                    battery -= visited[nx][ny]
                    if battery < 0:
                        sign = 1
                        return
                    else:
                        battery += visited[nx][ny] * 2
                        board[nx][ny].remove(-passenger)
                        board[nx][ny].append(-1000)
                    return True
    return False
sign = 0
while 1:
    if is_Finished() == True or sign == 1:
        break
    car_x, car_y = find_car()
    passenger_x, passenger_y = find_passenger(car_x, car_y)
    if battery <= 0:
        sign = 1
        break
    if passenger_x == -1:
        sign = 1
        break
    elif passenger_x != -1:
        if move_passenger(passenger_x, passenger_y) == False:
            sign = 1

if sign == 1:
    print(-1)
else:
    print(battery)