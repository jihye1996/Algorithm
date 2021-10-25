import sys
import heapq

input = sys.stdin.readline
answer, cnt = 0, 0
V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
heap = [[0, 1]] # 비용, V

for _ in range(E):
    v1, v2, g = map(int, input().split())
    graph[v1].append([g, v2])
    graph[v2].append([g, v1])

while heap:
    if cnt == V:
        break
    
    g, v = heapq.heappop(heap)
    if not visited[v]:
        visited[v] = True
        answer += g
        cnt += 1
        
        for t in graph[v]:
            heapq.heappush(heap, t)
        

print(answer)
