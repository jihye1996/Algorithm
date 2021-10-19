# 2021.01.19: 수정필요
from collections import defaultdict
import heapq

INF = int(1e9)
N = int(input())
M = int(input())
bus = defaultdict(list)
distances = [INF] * (N+1)

for _ in range(M):
    s, e, c = map(int, input().split())
    bus[s].append((e, c))

start, end = map(int, input().split())

queue = []
heapq.heappush(queue, (0, start))

while 0 < len(queue):
    cost, city = heapq.heappop(queue)
    
    if distances[city] < cost:
        continue
    
    for b in bus[city]:
        if cost + b[1] < distances[b[0]]:
            distances[b[0]] = cost + b[1]
            heapq.heappush(queue, (cost + b[1], b[0]))
print(distances[end])
