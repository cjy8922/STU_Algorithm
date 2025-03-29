import sys
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1 ,-1 ,-1 ,0, 1]
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
board_tonic = [[0] * n for _ in range(n)]
board_tonic[-1][0], board_tonic[-2][0], board_tonic[-1][1], board_tonic[-2][1] = 1, 1, 1, 1
move_rule = []
for _ in range(m):
    d, p = map(int, input().split())
    move_rule.append((d-1, p))
answer = 0
check_tonic = []

def move_tonic(turn):
    global board_tonic
    test = [[0] * n for _ in range(n)]
    d, p = move_rule[turn]
    for i in range(n):
        for j in range(n):
            if board_tonic[i][j] == 1:
                nx, ny = i, j
                for _ in range(p):
                    nx = (nx + dx[d] + n) % n
                    ny = (ny + dy[d] + n) % n
                test[nx][ny] = 1
                check_tonic.append((nx, ny))
    board_tonic = test

def inject_tonic():
    for i in range(n):
        for j in range(n):
            if board_tonic[i][j] == 1:
                board[i][j] += 1

def grow_tree():
    for x, y in check_tonic:
        cnt = 0
        for k in range(1, 8, 2):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                cnt += 1
        board[x][y] += cnt

def cut_tree():
    global answer, check_tonic
    next_tonic = []
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and (i, j) not in check_tonic:
                board[i][j] -= 2
                next_tonic.append((i, j))
    check_tonic = next_tonic

def new_tonic():
    global board_tonic
    test= [[0] * n for _ in range(n)]
    for x, y in check_tonic:
        test[x][y] = 1
    board_tonic = test
    check_tonic.clear()

for turn in range(m):
    move_tonic(turn)
    inject_tonic()
    grow_tree()
    cut_tree()
    new_tonic()
    
for i in range(n):
    for j in range(n):
        if board[i][j] > 0:
            answer += board[i][j]
print(answer)