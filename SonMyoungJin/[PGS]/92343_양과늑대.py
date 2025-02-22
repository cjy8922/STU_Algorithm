#01:02:40.45
'''
양과 늑대의 수를 세면서 양의 수 >늑대의 수인 경우만 탐색해서 최대 가능한 양의 수 세는 문제
- 트리 구조에서 각 경로마다의 양과 늑대의 수를 추적하는데 특정 조건의 경우는 제외하므로 백트래킹 사용.
- BFS는 각 레벨별로 양과 늑대수 동시 추적해야함 => 추적 어려움.

1. 각 노드 방문 여부를 추적하기 위해 visited bool형 list로 선언.
    - 0번은 항상 방문하므로 visited[0] = True로 초기화
2. 현재 노드(cur)를 기준으로 DFS
    - 현재 노드 양인지 늑대인지 확인 후 마릿수 반영
    - 양<=늑대 인지 확인 필요 -> True이면, 탐색 안하니까 return으로 종료
    - 위에 조건 체크되면 현재 마릿수가 최대 이면 저장
    - egdes가 [부모노드(p) == cur, 자식노드(c)]를 나열한 배열이기 때문에 부모노드 방문했을 때, 자식노드 방문하지 않았다면 방문.
        - 재귀적으로 자식노드(c)를 현재 노드(cur)로 다시 DFS
    - DFS가 return 되면 유효하지 않은 경로이므로 다른 경로를 탐색하도록, 자식노드를 False로 만들어 방문하지 않은 상태로 백트래킹.
        - 다른 노드를 탐색하다가 다시 방문 가능 할 수도 있음
        
(cur 변수는 굳이 안쓰고 p로 접근해도 괜찮을 듯)
'''
answer = 0
def dfs(cur, num_w, num_s, visited, info, edges):
    global answer
    if info[cur] == 0:
        num_s += 1
    else:
        num_w += 1
    
    # 늑대의 수가 양의 수보다 많거나 같으면 안됨
    if num_w >= num_s:
        return
    
    # 최대 양 마릿수를 저장
    answer = max(answer, num_s)
    
    # 현재 노드에서 갈 수 있는 노드 탐색
    for p, c in edges:
        if visited[p] and not visited[c]:
            visited[c] = True
            dfs(c, num_w, num_s, visited, info, edges)
            visited[c] = False
            
def solution(info, edges):
    global answer
    visited = [False] * (len(info))
    visited[0] = True
    dfs(0, 0, 0, visited, info, edges)
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
#info = [0,1,0,1,1,0,1,0,0,1,0]
#edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

print(solution(info, edges))

'''
이게 더 간단한 듯.
참고 코드 : https://talktato.tistory.com/62

1. cur(현재 노드) 사용안하고 => visited[p]가 현재 노드
2. info[c] 미리 확인해 수 갱신 => info[c]이 양인지 늑대인지 보고 수 증가시켜 DFS
3. 늑대>=양 이면 return 으로 종료 => 양<늑대 일때만 양의 수 기록하고 탐색 진행
4. global로 answer 최대일때마다 값 갱신 => answer 리스트로 양의 수 계속 기록하고 최대값 return

def dfs(num_w, num_l, visited, info, edges, answer):
    if num_w < num_l:
        answer.append(num_l)
    else:
        return

    for p, c in edges:
        if visited[p] and not visited[c]:
            visited[c] = True
            if info[c] == 0:
                dfs(num_w, num_l + 1, visited, info, edges, answer)
            else:
                dfs(num_w + 1, num_l, visited, info, edges, answer)
            visited[c] = False

def solution(info, edges):
    answer = []
    visited = [False] * (len(info))
    visited[0] = True
    dfs(0, 1, visited, info, edges, answer)
    return max(answer)
'''