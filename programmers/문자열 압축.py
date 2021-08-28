import math

def solution(s):
    answer = len(s)
    stack = []
    
    for v in range(1, len(s)//2 + 1):
        s_split = [s[i:i+v] for i in range(0, len(s), v)]
        count = 1
        compress = ''
        for a, b in zip(s_split, s_split[1:] + ['']):
            if a == b:
                count += 1
            else:
                if 1 < count:
                    compress += str(count) + a
                    count = 1
                else:
                    compress += a
        answer = min(answer, len(compress))
    return answer

#use stack
'''
import math

def solution(s):
    answer = len(s)
    stack = []
    for v in range(1, len(s)//2 + 1):
        s_split = [s[i:i+v] for i in range(0, len(s), v)]
        count = 1
        for s_v in s_split + ['']:
            if len(stack) == 0:
                stack.append(s_v)
            else:
                top = stack.pop()
                if top == s_v:
                    count += 1
                    stack.append(top)
                else:
                    if count == 1:
                        stack.append(top)
                        stack.append(s_v)
                    else:
                        stack.append(str(count))
                        stack.append(top)
                        stack.append(s_v)
                    count = 1
        answer = min(answer, len(''.join(stack))) 
        stack.clear()   
    return answer
'''
