#01:16:41.16
import sys

#sys.stdin = open('input.txt','r')

def input():
    return sys.stdin.readline().rstrip()

'''
1. 넘어트렸던 도미노를 세울 수도 있기 때문에 넘어진 상태(status)와 도미노 길이 보드(board)를 각각 따로 관리
2. 넘어트리는 도미노 길이만큼 연쇄적으로 넘어짐
    - length = board[x][y]로 받고, 
    - while문을 이용해 length를 갱신하고, length-=1씩해가면서 도미노를 연쇄적으로 넘어트림.
3. 넘어진 도미노 갯수만큼 공격 점수 얻음.
'''

N, M, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
status = [['S'] * M for _ in range(N)]
score = 0

directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}

for _ in range(R):
    # 공격
    x, y, d = input().split()
    x, y = int(x) - 1, int(y) - 1
    dx, dy = directions[d]
    
    if status[x][y] == 'S':
        length = board[x][y]
        nx, ny = x, y
        # 공격수가 넘어트린 도미노의 길이만큼 넘어짐
        while 0 <= nx < N and 0 <= ny < M and length > 0:
            if status[nx][ny] == 'S': # 현재 이 자리 도미노 세워져있으면
                status[nx][ny] = 'F' # 넘어트림
                score += 1
                # 더 긴 도미노 만나면 연쇄적으로 더 넘어져야하므로 도미노 길이 갱신
                length = max(length, board[nx][ny])
            nx += dx # 다음 도미노
            ny += dy
            length -= 1

    # 수비       
    x, y = map(lambda v: int(v) - 1, input().split())
    status[x][y] = 'S'

print(score)
for row in status:
    print(' '.join(row))