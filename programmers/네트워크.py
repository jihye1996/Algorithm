def solution(n, computers):
    answer = 0
    queue = []
    visited = [False]*n
    
    for i in range(n):
        if visited[i] == False:
            queue.append(i)
            answer+=1
            #bfs
            while(0 < len(queue)):
                front = queue.pop(0)
                visited[front] = True
                for j in range(n):
                    if computers[front][j] == 1 and visited[j] == False:
                        queue.append(j)
    return answer
