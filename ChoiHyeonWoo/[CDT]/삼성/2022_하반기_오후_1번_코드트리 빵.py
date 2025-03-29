from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_people = [[[] for _ in range(n)]for _ in range(n)]
#베이스 캠프 : 1000
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            board[i][j] = 1000
for i in range(1, m + 1):
    x, y = map(int, input().split())
    board[x-1][y-1] = i
time = 1

def is_Finished():
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                return False
    return True

def find_store(people):
    for i in range(n):
        for j in range(n):
            if board[i][j] == people:
                return i, j

def move_people():
    global cant_move, move
    for i in range(n):
        for j in range(n):
            if board_people[i][j]:
                while board_people[i][j]:
                    people = board_people[i][j].pop()
                    store_x, store_y = find_store(people)
                    Q = deque()
                    Q.append((store_x, store_y))
                    visited = [[0] * n for _ in range(n)]
                    visited[store_x][store_y] = 1
                    sign = 0
                    while Q:
                        temp = Q.popleft()
                        for k in range(4):
                            nx = temp[0] + dx[k]
                            ny = temp[1] + dy[k]
                            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                                if board[nx][ny] < 0:
                                    if board[nx][ny] == -1000 and temp[0] == store_x and temp[1] == store_y:
                                        sign = 1
                                        move_x, move_y = temp[0], temp[1]
                                        break
                                    else:
                                        continue
                                if nx == i and ny == j:
                                    sign = 1
                                    move_x, move_y = temp[0], temp[1]
                                    break
                                Q.append((nx, ny))
                                visited[nx][ny] = 1
                        if sign == 1:
                            break
                    if sign == 0:
                        # for x in board_people:
                        #     print(x, end = ' ')
                        #     print()
                        # print('--------------------')
                        # for x in board:
                        #     print(x, end =' ')
                        #     print()
                        print(people, i, j, store_x, store_y, 43587456)
                    if move_x == store_x and move_y == store_y:
                        cant_move.append((store_x, store_y))
                    else:
                        # board_people[move_x][move_y].append(people)
                        move.append((people, move_x, move_y))

def go_base(people):
    for i in range(n):
        for j in range(n):
            if board[i][j] == people:
                visited = [[-1] * n for _ in range(n)]
                visited[i][j] = 0
                Q = deque()
                Q.append((i, j))
                base = []
                while Q:
                    temp = Q.popleft()
                    for k in range(4):
                        nx = temp[0] + dx[k]
                        ny = temp[1] + dy[k]
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and board[nx][ny] >= 0:
                            Q.append((nx, ny))
                            visited[nx][ny] = visited[temp[0]][temp[1]] + 1
                            if board[nx][ny] == 1000:
                                base.append((visited[nx][ny], nx, ny))
                base.sort(key = lambda x : (x[0], x[1], x[2]))
                base_x, base_y = base[0][1], base[0][2]
                board_people[base_x][base_y].append(people)
                # board[base_x][base_y] = -1000
                cant_move.append((base_x, base_y))
while 1:
    cant_move = []
    move = []
    move_people()
    if cant_move:
        for x, y in cant_move:
            board[x][y] = -board[x][y]
    if move:
        for people, x, y in move:
            board_people[x][y].append(people)
    cant_move = []
    if time <= m:
        go_base(time)
    if is_Finished() == True:
        print(time)
        break
    time += 1
    if cant_move:
        for x, y in cant_move:
            board[x][y] = -board[x][y]