def solution(answers):
    answer = [0, 0, 0]
    returnValue = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, v in enumerate(answers):
        if v == one[i%5]:
            answer[0]+=1
        if v == two[i%8]:
            answer[1]+=1
        if v == three[i%10]:
            answer[2]+=1

    for i in range(3):
        if max(answer) == answer[i]:
            returnValue.append(i+1)
    
    return returnValue
