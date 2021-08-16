import math

def solution(progresses, speeds):
    data = []
    current = 0
    
    for p, s in zip(progresses, speeds):
        if len(data) == 0 or current < math.ceil((100-p) / s):
            data.append(1)
            current = math.ceil((100-p) / s)
        else:
            data[-1] += 1
                  
    return data
'''
import math

def solution(progresses, speeds):
    answer = []
    rests = []
    for p, s in zip(progresses, speeds):
        rests.append(math.ceil((100-p) / s))

    print(rests)
    count = 1
    current = rests[0]
    for i in range(1, len(rests)):
        if current < rests[i]:
            current = rests[i]
            answer.append(count)
            count = 1
        else:
            count+=1
            
            
    answer.append(count)       
    return answer
 '''
