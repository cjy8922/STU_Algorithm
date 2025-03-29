import sys
input = sys.stdin.readline
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
n, M, k = map(int, input().split())
board = [[[] for _ in range(n)]for _ in range(n)]
for _ in range(M):
    x, y, m, s, d = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y].append((m, s, d))

def move_atom():
    global board
    test_board = [[[] for _ in range(n)]for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for k in range(len(board[i][j])):
                    m, s, d = board[i][j][k][0], board[i][j][k][1], board[i][j][k][2]
                    nx, ny = i, j
                    for _ in range(s):
                        nx = (nx + dx[d] + n) % n
                        ny = (ny + dy[d] + n) % n
                    test_board[nx][ny].append((m, s, d))
    board = test_board

def compose_atom():
    for i in range(n):
        for j in range(n):
            if board[i][j] and len(board[i][j]) >= 2:
                M, S = 0, 0
                check = board[i][j][0][2] % 2
                sign = 0
                for k in range(len(board[i][j])):
                    M += board[i][j][k][0]
                    S += board[i][j][k][1]
                    if check != board[i][j][k][2] % 2:
                        sign = 1
                M = M // 5
                S = S // len(board[i][j])
                if M == 0:
                    board[i][j] = []
                    continue
                if sign == 0:
                    board[i][j] = []
                    for k in range(0, 7, 2):
                        board[i][j].append((M, S, k))
                else:
                    board[i][j] = []
                    for k in range(1, 8, 2):
                        board[i][j].append((M, S, k))

def count_m():
    M = 0
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                for k in range(len(board[i][j])):
                    M += board[i][j][k][0]
    return M


for test_case in range(1, k+1):
    move_atom()
    compose_atom()
print(count_m())