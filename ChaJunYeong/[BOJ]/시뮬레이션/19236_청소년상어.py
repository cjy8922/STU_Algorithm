import sys
def input():
    return sys.stdin.readline().rstrip()


"""
    # 1
    청소년 상어는 (0, 0)에 있는 물고기를 먹고 (0, 0)에 위치하게 됨
    이후, 상어의 방향은 (0, 0) 물고기 방향과 동일

    # 2
    이후 물고기 이동. 이때, 물고기는 번호가 작은 물고기부터 순서대로 이동.
    한칸 이동할 수 있음
        - 이때, 빈 칸, 다른 물고기가 있는 칸만 이동 가능. 다른 물고기가 있는 경우, 서로의 위치 스위치
        - 상어가 있거나 범위 밖을 벗어날 순 없음
    방향을 이동할 수 있는 칸을 향할때까지 45도 반시계 회전
    이동할 수 없으면 이동하지 않음

    # 3.
    상어 이동. 주어진 방향으로만 이동. (한번에 여러 칸 이동 가능)
    물고기가 있는 칸으로 이동하면, 그 칸의 물고기를 먹고 방향 흡수
    이동 중 지나가는 칸에 있는 물고기는 먹지 않음.
    물고기가 없는 칸은 이동 불가.
    이동할 수 있는 칸이 없으면 공간에서 벗어남.

    먹을 수 있는 물고기 번호의 최댓값 구하기
"""

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

# 초기 세팅
board = [[0] * 4 for _ in range(4)]
fish_info = dict()

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish_idx = data[j * 2]
        fish_dir = data[j * 2 + 1] - 1
        board[i][j] = fish_idx
        fish_info[fish_idx] = [i, j, fish_dir]




# 상태 저장을 위한 딥카피 구현
def deepcopy_board(b):
    return [row[:] for row in b]


def deepcopy_fishinfo(d):
    new_info = {}
    for k, v, in d.items():
        new_info[k] = v[:] if v is not None else None
    return new_info


# 물고기 움직임
def fish_move(board, fish_info):
    for i in range(1, 17):
        if fish_info[i] is None:
            continue

        fish_y, fish_x, fish_d = fish_info[i]
        for _ in range(8):
            ny, nx = fish_y + dy[fish_d], fish_x + dx[fish_d]

            # 범위 내, 상어와 마주치지 않으면 움직임
            if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx] != -1:
                target = board[ny][nx]
                board[fish_y][fish_x], board[ny][nx] = target, i
                fish_info[i] = [ny, nx, fish_d]
                if target != 0: # 물고기가 있는 경우
                    fish_info[target][0], fish_info[target][1] = fish_y, fish_x
                break

            fish_d = (fish_d + 1) % 8


# 상어 움직임
max_answer = 0
def dfs(board, fish_info, shark_y, shark_x, shark_d, total):
    global max_answer

    # 상태 복사
    board = deepcopy_board(board)
    fish_info = deepcopy_fishinfo(fish_info)

    # 물고기 움직임
    fish_move(board, fish_info)

    # 상어 움직임
    for step in range(1, 4):
        ny, nx = shark_y + dy[shark_d] * step, shark_x + dx[shark_d] * step
        
        # 범위 내, 물고기가 있으면 움직임
        if 0 <= ny < 4 and 0 <= nx < 4 and board[ny][nx] != 0:
            fish_idx = board[ny][nx]
            nd = fish_info[fish_idx][-1]

            # 상어 상태 업데이트
            new_board = deepcopy_board(board)
            new_fish_info = deepcopy_fishinfo(fish_info)
            new_board[shark_y][shark_x] = 0
            new_board[ny][nx] = -1
            new_fish_info[fish_idx] = None

            # 재귀 탐색
            dfs(new_board, new_fish_info, ny, nx, nd, total + fish_idx)

    max_answer = max(max_answer, total)

init_fish = board[0][0]
shark_d = fish_info[init_fish][-1]
total = init_fish
fish_info[init_fish] = None
board[0][0] = -1
dfs(board, fish_info, 0, 0, shark_d, total)
print(max_answer)