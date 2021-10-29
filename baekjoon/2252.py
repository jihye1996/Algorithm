import sys
from collections import deque


def topoloy_sort(graph, degree):
    answer = []
    q = deque()
        
    for i in range(1, N+1):
        if 0 == degree[i]:
            q.append(i)
            
    while q:
        t = q.popleft()
        answer.append(t)
        
        for E in graph[t]:
            degree[E] -= 1
            
            if degree[E] == 0:
                q.append(E)
    
    for i in answer[::-1]:
        print(i, end=' ')
    
        
        
input = sys.stdin.readline

N, M = map(int, input().split())
degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[y].append(x)
    degree[x] += 1
    
topoloy_sort(graph, degree)
