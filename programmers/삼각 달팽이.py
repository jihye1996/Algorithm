def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)] #2차원배열
    
    num = 1
    x, y = -1, 0
    for step in range(n):
        for j in range(n-step):
            if step % 3 == 0: #하
                x+=1
            elif step % 3 == 1:#우
                y+=1
            else:#상
                x-=1
                y-=1
            answer[x][y] = num
            num +=1       
    return sum(answer, []) #2차원배열 -> 1차원배열
