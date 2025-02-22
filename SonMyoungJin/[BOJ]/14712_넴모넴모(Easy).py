#01:57:58.29
import sys

#sys.stdin = open('input.txt', 'r')
'''
시간 초과로 인해 코드 참고함.
코드 참고: https://github.com/tony9402/baekjoon/blob/main/solution/backtracking/14712/main.py

넴모 놓았을 때, 2*2가 없으면 게임 그만두는데 이 때 가능한 모든 배치 찾아라
=> 주어진 그리드에서 넴모 배치한 후 2*2 사각형을 만들지 않는 경우만을 세는 문제

1. 가능한 모든 넴모 배치를 탐색해야하는데, 2*2가 생기는 불필요한 경로를 제외해야하므로 백트래킹 방식 사용.
2. 넴모는 그리드에 놓이거나 안놓이므로 2차원 bool 배열 grid로 정의, 경우의 수를 추적하기 위해 answer 정의.
3. 넴모를 그리드에 놓는 함수 nemmo를 정의하고, 2D를 1D 인덱스로 접근하기 위해서 
    현재까지 탐색한 칸의 수 cnt를 파라미터로 받음.
    - cnt로 현재 위치(row, col) 계산
    - 현재 위치에서 넴모 놓지 않는 경우는 nemmo(cnt+1)해서 다음칸 접근
    - 현재 위치에서 넴모 놓는 경우는 놓는 순간 2*2 생기는지 확인하고
        안생기면 다음칸 접근해서 dfs, 생기면 불필요한 경로이므로 현재위치 False 표시해 방문 안하는 걸로
4. 2*2 사각형 체크하는 함수 따로 빼서 관리
    - 현재 위치에 넴모 놓았을 때 2*2 사각형 만들어지는지 확인하면 되기 때문에
        현재 위치가 (1,1)이상일 때, 왼쪽위, 위, 왼쪽 각각 확인
        (0,0) (0,1) (1,0)일때는 어차피 안 만들어지니까      

'''
N, M = map(int, sys.stdin.readline().split())
grid = [[False]* M for _ in range(N)]
answer = 0

# 현재 위치에 넴모 놓았을 때 2*2 사각형 만들어지는지 확인
def is_square(row, col):
    if row > 0 and col > 0: #왼쪽 위, 위, 왼쪽 확인하려고
        if grid[row-1][col-1] and grid[row-1][col] and grid[row][col-1]:
            return True
    return False

def nemmo(cnt):
    global answer # 변경하려고 전역변수로 선언
    
    if cnt == N * M: # 모든 칸 탐색했을 때 => 2*2 안만들어서 유효한 배치일테니까 경우의 수 증가
        answer += 1
        return
    
    # 현재 위치 계산
    row = cnt // M
    col = cnt % M
    
    # 현재 위치(row, col)에 넴모 놓지 않는 경우 탐색
    # 넴모 안 놓고 다음 위치로(cnt+1) 
    nemmo(cnt + 1)
    # 현재 위치(row, col)에 넴모 놓았을 경우 탐색
    grid[row][col] = True
    if not is_square(row, col): # 2*2 안만들어지면 dfs 탐색
        nemmo(cnt + 1)
    grid[row][col] = False # 2*2 만들어지니까 불필요한 경로이므로 백트래킹
    
nemmo(0)
print(answer)
    
'''
# 시간초과!!
------------------------------------------------------------------------
문제점 => 개선점
1. nemmo(grid, N, M, row, col) 형태로 2차원 배열 grid를 계속 재귀적으로 호출
    => 코드 참고하여 cnt(현재까지 처리한 칸)로 현재 위치(row, col)를 추적하여 개선
2. is_square 함수가 매번 grid 모든 칸을 탐색해 2*2 사각형 찾음
    => 해당 위치에 넴모 놓음으로써 2*2 사각형 생기는지만 확인하면 되므로
        해당 위치에서 왼쪽위, 위, 왼쪽만 확인하는 것으로 개선
------------------------------------------------------------------------
# 현재 위치에 넴모 놓았을 때 2*2 사각형 만들어지는지 확인
def is_square(grid, N, M):
    for i in range(N-1):
        for j in range(M-1):
            if grid[i][j] and grid[i+1][j] and grid[i][j+1] and grid[i+1][j+1]:
                # 2*2 사각형 만들어지면 True
                return True
    return False
    
def nemmo(grid, N, M, row, col):
    if row == N: #끝까지 도달
        # 2*2 사각형 만들어지지 않았다면 경우의 수 1
        if not is_square(grid, N, M):
            return 1
        return 0
    
    # 오른쪽으로 1칸이동, 열 끝까지 도달하면 다음 행으로
    next_row = row
    next_col = col + 1
    if next_col == M:
        next_row += 1
        next_col = 0
    
    result = 0
    # 현재 위치(row, col)에 넴모 놓지 않는 경우
    result += nemmo(grid, N, M, next_row, next_col)
    
    # 현재 위치(row, col)에 넴모 놓았을 때
    grid[row][col] = True
    result += nemmo(grid, N, M, next_row, next_col)
    grid[row][col] = False # 넴모 제거
    
    return result

print(nemmo(grid, N, M, 0, 0))
'''