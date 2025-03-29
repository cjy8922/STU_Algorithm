import sys
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
input = sys.stdin.readline
n, m, k, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if board[i][j] == -1:
            board[i][j] = -1000
check_blank = []
answer = 0

def grow_tree():
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = 0
                for k in range(0, 7, 2):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > 0:
                        cnt += 1
                board[i][j] += cnt

def spread():
    test = [[0] * n for _ in range(n)]
    spread_tree = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                check = []
                cnt = 0
                for k in range(0, 7, 2):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        cnt += 1
                        check.append((nx, ny))
                if check:
                    for x, y in check:
                        test[x][y] += board[i][j] // cnt
                        if (x, y) not in spread_tree:
                            spread_tree.append((x, y))
    for x, y in spread_tree:
        board[x][y] = test[x][y]

def kill(spray):
    x, y = spray
    board[x][y] = -c - 1
    for q in range(1, 8, 2):
        nx = x
        ny = y
        for _ in range(k):
            nx = nx + dx[q]
            ny = ny + dy[q]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == -1000:
                    break
                elif board[nx][ny] <= 0:
                    board[nx][ny] = -c - 1
                    break
                else:
                    board[nx][ny] = -c - 1

def spray_weedkiller():
    global answer
    spray = (-1, -1)
    check = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                cnt = board[i][j]
                for q in range(1, 8, 2):
                    nx = i
                    ny = j
                    for _ in range(k):
                        nx = nx + dx[q]
                        ny = ny + dy[q]
                        if 0 <= nx < n and 0 <= ny < n:
                            if board[nx][ny] <= 0: break
                            elif board[nx][ny] > 0:
                                cnt += board[nx][ny]
                check.append((cnt, i, j))
    if check:
        check.sort(key = lambda x : (-x[0], x[1], x[2]))
        spray = (check[0][1], check[0][2])
        kill(spray)
        answer += check[0][0]
                                
def count_weedkiller():
    for i in range(n):
        for j in range(n):
            if board[i][j] < 0 and board[i][j] != -1000:
                board[i][j] += 1

for turn in range(1, m + 1):
    count_weedkiller()
    grow_tree()
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print(' ')
    spread()
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print('')
    spray_weedkiller()
    # for x in board:
    #     print(x, end = ' ')
    #     print()
    # print('-----------------------')

print(answer)