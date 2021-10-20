# 2021.10.20

import sys
import heapq

input = sys.stdin.readline
answer = 0
V, E = map(int, input().split())
graph = []
visited = [False] * E

for _ in range(E):
    v1, v2, g = map(int, input().split())
    heapq.heappush(graph, (g, v1, v2))

connected = 0
# 수정 필요 
while graph or connected < V - 1:
    
    g, v1, v2 = heapq.heappop(graph)
    if visited[v1-1] and visited[v2-1]:
        continue
    else:
        visited[v1-1], visited[v2-1] = True, True
        answer += g
        connected += 1

print(answer)
