def solution(routes):
    answer = []
    routes.sort()
    #print(routes)
    for x, y in routes:
        if len(answer)==0:
            answer.append([x,y])
        if x < answer[-1][1]:
            answer[-1][0] = max(answer[-1][0], x)
            answer[-1][1] = min(answer[-1][1], y)
        else:
            answer.append([x,y])
    #print(answer)
    return len(answer)
