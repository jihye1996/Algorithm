from collections import defaultdict
import heapq
import sys 
input = sys.stdin.readline 

'''
3, 4 번 라인을 사용해서 N번의 반복문을 돌 때 속도 개선 가능
N (= 10,000,000) 기준, readline 없이 실행하면 약 12초, readline 사용 시 4초로 단축 가능
ref: https://www.acmicpc.net/blog/view/56
'''

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
