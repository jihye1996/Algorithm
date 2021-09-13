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

'''
# retry 21.09.13
def solution(n, edge):
    answers = [0] * (n+1)
    visit = [False] * (n+1)
    nodes = {i: [] for i in range(1,n+1)}
    queue = [1]
    for x, y in edge:
        nodes[x].append(y)
        nodes[y].append(x)

    while 0 < len(queue):
        front = queue.pop(0)
        visit[front] = True
        for v in nodes[front]:
            if visit[v] == False and v not in queue:
                queue.append(v)
                answers[v] = answers[front] + 1
    max_value = max(answers)
    return answers.count(max_value)
'''
