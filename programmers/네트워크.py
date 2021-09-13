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
retry 21.09.13 dfs with queue
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
 
retry 21.09.13 dfs with stack
def solution(n, computers):
    answer = 0
    visit = [False] * n
    stack = []
    for i in range(n):
        if visit[i] == False:
            stack.append(i)
            answer += 1
            
            while 0 < len(stack):
                top = stack.pop()
                visit[top] = True
                for j in range(n):
                    if computers[top][j] == 1 and visit[j] == False:
                        stack.append(j)
    return answer
    
retry 21.09.13 dfs with recursive
def dfs(root, visit, computers):
    
    visit[root] = True
    for j in range(len(visit)):
        if computers[root][j] and not visit[j]:
            dfs(j, visit, computers)

def solution(n, computers):
    answer = 0
    visit = [False] * n
    
    for i in range(n):
        if visit[i] == False:
            answer += 1
            dfs(i, visit, computers)
            
    return answer
'''
