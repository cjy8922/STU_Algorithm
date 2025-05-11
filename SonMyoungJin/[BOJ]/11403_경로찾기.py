#00:51:26.15
import sys
from collections import deque

#sys.stdin = open("input.txt", 'r')

def input():
    return sys.stdin.readline().rstrip()

'''
N개의 정점과 해당하는 인접행렬 주어졌을 때, 정점 i에서 j로 가는 길이 있으면 1로 없으면 0으로 출력하는 문제
- 정점 i에서 j까지의 길이 있는지 찾는데, 인접한 정점을 계속 탐색하기 위해 BFS 사용.
1. 모든 정점을 확인해야하므로 for문 중첩(i, j)으로 모두 탐색
2. 방문할 수 있는 노드(도달 가능한)를 표시하기 위해 visited 배열 사용
'''

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * N for _ in range(N)]

for i in range(N):
    visited = [False] * N
    queue = deque([i])
    
    while queue:
        cur = queue.popleft()
        for j in range(N):
            if G[cur][j] == 1 and not visited[j]:
                queue.append(j)
                visited[j] = True
                
    # visited에 도달 가능 여부가 저장되어 있으니까
    for j in range(N):
        if visited[j]:
            answer[i][j] = 1

for row in answer:
    print(*row)