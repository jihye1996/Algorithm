def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1: x[1]])[x[2]-1], commands))
    '''
    answer = []
    for x, y, i in commands:
        answer.append(sorted(array[x-1:y])[i-1])
    return answer
    '''
