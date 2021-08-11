def solution(record):
    dict = {'Enter': '님이 들어왔습니다.',
           'Leave':'님이 나갔습니다.'}
    
    answer = []
    
    for r in record:
        str = r.split(' ')
        if str[0] != 'Leave':
            dict[str[1]] = str[2]
    #print(dict)
    for r in record:
        str = r.split(' ')
        if str[0] != 'Change':
            answer.append(dict[str[1]] +dict[str[0]])
    #print(answer)
    return answer
