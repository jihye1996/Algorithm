def solution(m, n, puddles):
    maps = [[1 for j in range(m)] for i in range(n)]

    if puddles != [[]]:  
        for p in puddles:
            maps[p[1]-1][p[0]-1] = 0
            
    for i in range(n):
        for j in range(m):
            if i == j == 0 or maps[i][j] == 0:
                continue
            if i == 0:
                maps[i][j] = maps[i][j-1]
            elif j == 0:
                maps[i][j] = maps[i-1][j]
            else:
                maps[i][j] = (maps[i-1][j] + maps[i][j-1]) % 1000000007

    return maps[n-1][m-1]
'''
def solution(m, n, puddles):
    maps = [[1 for j in range(m)] for i in range(n)]
    
    if puddles != [[]]:  
        for p in puddles:
            maps[p[1]-1][p[0]-1] = 0
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 0:
                if i == 0 and j == 0:
                    continue
                elif i == 0  and j != 0:
                    maps[i][j] = maps[i][j-1]
                elif i != 0  and j == 0:
                    maps[i][j] = maps[i-1][j]
                else:
                    maps[i][j] = (maps[i-1][j] + maps[i][j-1]) % 1000000007

    return maps[n-1][m-1]
'''
