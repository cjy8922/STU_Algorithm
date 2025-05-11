from collections import deque
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dx_bfs = [-1, 0, 1, 0]
dy_bfs = [0, -1, 0, 1]
m, t = map(int, input().split())
board_pack_man = [[0] * 4 for _ in range(4)]
r, c = map(int, input().split())
board_pack_man[r-1][c-1] = -1
board_monster = [[[] for _ in range(4)] for _ in range(4)]
board_copy = [[[] for _ in range(4)] for _ in range(4)]
eat = -1243256
pack_man = ()
pack_man_move_xy = []
for _ in range(m):
    r, c, d = map(int, input().split())
    board_monster[r-1][c-1].append(d)

def try_copy():
    for i in range(4):
        for j in range(4):
            if board_monster[i][j]:
                for k in range(len(board_monster[i][j])):
                    board_copy[i][j].append(board_monster[i][j][k])

def move_monster():
    for i in range(4):
        for j in range(4):
            if board_monster[i][j]:
                board_monster[i][j] = deque(board_monster[i][j])
                while board_monster[i][j]:
                    d = board_monster[i][j].popleft()
                    for k in range(d, d + 8):
                        k = (k + 7) % 8 + 1
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0 <= nx < 4 and 0 <= ny < 4 and board_pack_man[nx][ny] != -1 and -1 not in board_monster[nx][ny]:
                            board_monster[nx][ny].append(k)

def DFS(x, y, visited, maximum, move_cnt, test):
    global eat, pack_man, pack_man_move_xy
    if move_cnt == 3:
        if maximum > eat:
            eat = maximum
            pack_man = (x,y)
            pack_man_move_xy = test

    else:
        for i in range(4):
            nx = x + dx_bfs[i]
            ny = y + dy_bfs[i]
            if 0 <= nx < 4 and 0 <= ny < 4 and visited[nx][ny] == 0:
                cnt = 0
                for j in board_monster[nx][ny]:
                    if j != -1:
                        cnt += 1
                test.append((nx, ny))
                visited[nx][ny] = 1
                DFS(nx, ny, visited, maximum + cnt, move_cnt + 1, test)
                visited[nx][ny] = 0

def move_pack_man():
    global pack_man_move_xy, pack_man, eat
    for i in range(4):
        for j in range(4):
            if board_pack_man[i][j] == -1:
                visited = [[0] * 4 for _ in range(4)]
                DFS(i, j, visited, 0, 0, [])
                for x ,y in pack_man_move_xy:
                    if board_monster[x][y]:
                        board_monster[x][y].clear()
                        board_monster[x][y].append(-1)
                board_pack_man[i][j] = 0
                if pack_man:
                    x, y = pack_man
                    board_pack_man[x][y] = -1
                pack_man = ()
                pack_man_move_xy = []
                eat = 0

def remove_dead_body():
    for i in range(4):
        for j in range(4):
            if board_monster[i][j]:
                if -1 in board_monster[i][j]:
                    board_monster[i][j] = []

def born_copy():
    for i in range(4):
        for j in range(4):
            if board_copy[i][j]:
                board_copy[i][j] = deque(board_copy[i][j])
                while board_copy[i][j]:
                    d = board_copy[i][j].popleft()
                    board_monster[i][j].append(d)

for turn in range(t):
    try_copy()
    move_monster()
    move_pack_man()
    if turn % 2 == 0:
        remove_dead_body()
    born_copy()
answer = 0
for i in range(4):
    for j in range(4):
        if board_monster[i][j]:
            answer += len(board_monster[i][j])
print(answer)