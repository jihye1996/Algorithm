def solution(n, edge):
    answer = 0
    visited = [0 for i in range(n)] # for is visit and distance
    graph = {i:[] for i in range(1, n+1)}
    
    # make graph
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    # bfs
    queue = [1]
    visited[0] = 0
    while len(queue) != 0:
        c = queue.pop(0)
        for v in graph[c]:
            if visited[v-1] == 0 and v != 1:
                queue.append(v)
                visited[v-1] = visited[c-1] + 1

    return visited.count(max(visited))
