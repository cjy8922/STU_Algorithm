import sys
def input():
    return sys.stdin.readline().rstrip()

"""
    아기 상어 
        - 크기 2 / 1초에 상 하 좌 우 인접한 한 칸 씩 이동
        - 자신의 크기보다 큰 물고기는 지나갈 수 없음
        - 자신의 크기보다 작은 물고기는 먹을 수 있음
        - 자신의 크기와 같은 물고기는 먹을 순 없지만 지나갈 수 있음

        1. 더 이상 먹을 수 있는 물고기가 없으면 엄마 상어 도움
        2. 먹을 수 있는 물고기가 1이라면 해당 물고기 먹으러 감
        3. 먹을 수 있는 물고기가 더 많다면, 거리가 가장 가까운 물고기를 먹으러 감 - 열이 작은 순, 행이 작은 순
            - 거리 : 아기상어 - 물고기 칸으로 이동할 때 지나야하는 칸의 개수 최솟값
            - 먹을 수 있는 물고기가 있는 칸으로 이동하면, 이동과 동시에 물고기 먹음
            - 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
"""


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


# 상어의 상태 저장
shark_y, shark_x = 0, 0
for y in range(n):
    for x in range(n):
        if arr[y][x] == 9:
            shark_y, shark_x = y, x
            arr[shark_y][shark_x] = 0
shark_size = 2
shark_cnt = 0


# 상어의 먹이 탐색
from collections import deque
def bfs(sy, sx):
    q = deque()
    visited = [[0] * n for _ in range(n)]

    q.append((sy, sx))
    visited[sy][sx] = 1
    fish_pos = []

    while q:
        cy, cx = q.popleft()

        for dy, dx in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            ny, nx = cy + dy, cx + dx

            # 범위 내 방문하지 않은 경우,
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == 0:

                # 상어가 더 큰 경우
                if arr[ny][nx] < shark_size and arr[ny][nx] != 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    fish_pos.append((visited[ny][nx] - 1, ny, nx))

                # 상어와 사이즈가 같거나, 빈 공간일 경우
                if arr[ny][nx] == shark_size or arr[ny][nx] == 0:
                    visited[ny][nx] = visited[cy][cx] + 1
                    q.append((ny, nx))
    
    return sorted(fish_pos, key=lambda x: (x[0], x[1], x[2]))


ans = 0
while True:
    # 물고기 위치 받기
    fish_pos = bfs(shark_y, shark_x)

    # 남아 있는 물고기가 없으면
    if len(fish_pos) == 0:
        break

    # 맨 처음 물고기 먹기
    time, fish_y, fish_x = fish_pos[0]
    ans += time
    shark_cnt += 1
    arr[fish_y][fish_x] = 0
    shark_y, shark_x = fish_y, fish_x

    if shark_size == shark_cnt:
        shark_size += 1
        shark_cnt = 0

print(ans)

