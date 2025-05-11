import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    공격수 : 도미노 넘어뜨리기
    수비수 : 도미노 세우기

    1. N행 M열의 2차원 격자 모양 게임판에 도미노 세우기 (1이상 5이하 높이)
    2. 매 라운드 공격수가 먼저 공격 - 수비수는 공격 끝난 이후 수비
    3. 공격수
        - 특정 격자에 놓인 도미노를 동 / 서 / 남 / 북 중 원하는 방향으로 넘어뜨림
        - 길이가 K인 도미노가 특정 방향으로 넘어지면, 그 방향으로 K - 1개의 도미노가 넘어짐
        - 연쇄적으로 넘어짐
    4. 수비수
        - 넘어진 도미노들 중 원하는 것 하나를 세울 수 있음
    5. 총 r번의 라운드 동안 3 - 4 과정이 반복됨.
        - 매 라운드 넘어진 도미노 개수를 세고, r 라운드에 걸친 총합이 곧 점수
"""

n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 원본 도미노 deepcopy로 복사
board = [row[:] for row in arr]

# 게임 시작
from collections import deque
direction = {"N": [-1, 0], "E": [0, 1], "W": [0, -1], "S": [1, 0]}
ans = 0
for cnt in range(1, r + 1):
    ay, ax, ad = input().split()
    ay = int(ay) - 1
    ax = int(ax) - 1
    dy, dx = direction[ad]

    # 3. 공격수의 공격
    q = deque()
    q.append((arr[ay][ax], ay, ax))
    ans += 1
    arr[ay][ax] = 0

    while q:
        # 현재 쓰러뜨릴 도미노의 높이와 좌표
        h, y, x = q.popleft()

        for i in range(h):
            ny, nx = y + dy * i, x + dx * i

            # 쓰러뜨렸을 때, 범위 안이면서, 도미노가 세워져 있는 경우
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] != 0:
                q.append((arr[ny][nx], ny, nx))
                ans += 1
                arr[ny][nx] = 0
    
    # 4. 수비수의 방어
    dy, dx = map(int, input().split())
    dy -= 1
    dx -= 1
    arr[dy][dx] = board[dy][dx]


print(ans)
for y in range(n):
    for x in range(m):
        if arr[y][x] != 0:
            print("S", end=' ')
        else:
            print("F", end=' ')
    print()