def solution(s):
    stack = []
    
    for v in s:
        if len(stack) == 0:
            stack.append(v.upper())
        else:
            top = stack[-1]
            if top == ' ':
                stack.append(v.upper())
            else:
                stack.append(v.lower())
    return ''.join(stack)
