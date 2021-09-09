def solution(routes):
    routes.sort(key=lambda x: x[1])
    cur = -30001

    answer = 0
    for route in routes:
        if cur < route[0]:
            answer += 1
            cur = route[1]
    return answer
'''
def solution(routes):
    answer = []
    routes.sort()

    for x, y in routes:
        if len(answer)==0:
            answer.append([x,y])
        if x <= answer[-1][1]:
            answer[-1][0] = max(answer[-1][0], x)
            answer[-1][1] = min(answer[-1][1], y)
        else:
            answer.append([x,y])

    return len(answer)
'''
