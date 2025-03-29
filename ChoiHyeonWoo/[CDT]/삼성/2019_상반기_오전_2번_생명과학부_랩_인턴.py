import sys
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [[[] for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x, y, s, d, b = map(int, input().split())
    if d == 2:
        d = 3
    elif d == 3:
        d = 2
    board[x-1][y-1].append((s, d-1, b))
answer = 0
def collect_mold(x, y):
    global answer
    answer += board[x][y][0][-1]
    board[x][y].pop()

def move_mold():
    global board
    test = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                s, d, b = board[i][j][0][0], board[i][j][0][1], board[i][j][0][2]
                nx = i
                ny = j
                for _ in range(s):
                    nx = nx + dx[d]
                    ny = ny + dy[d]
                    if 0 > nx or n <= nx or 0 > ny or m <= ny:
                        d = (d + 2 + 4) % 4
                        nx = nx + (2 * dx[d])
                        ny = ny + (2 * dy[d])
                test[nx][ny].append((s, d, b))
    for i in range(n):
        for j in range(m):
            if len(test[i][j]) >= 2:
                test[i][j].sort(key = lambda x : -x[-1])
                live = test[i][j][0]
                test[i][j].clear()
                test[i][j].append(live)
    board = test
    
for j in range(m):
    for i in range(n):
        if board[i][j]:
            collect_mold(i, j)
            move_mold()
            break
    else:
        move_mold()
print(answer)