import heapq
inf = 999999999999999
V, E = map(int, input().split())
start = int(input())
distance = [inf] * (V + 1)
distance[start] = 0
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == inf:
        print('INF')
        continue
    print(distance[i])