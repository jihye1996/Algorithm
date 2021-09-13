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
'''
def solution(n, computers):
    answer = 0
    visit = [False] * n
    queue = []
    
    for i in range(n):
        if visit[i] == False:
            answer += 1
            queue.append(i)
            
            while 0 < len(queue):
                front = queue.pop(0)
                visit[front] = True
                for j in range(n):
                    if visit[j] == False and computers[front][j] == 1:
                        queue.append(j)
        #print(visit)
               
    return answer
'''
