def solution(prices):
    answer = [0 for i in range(len(prices))]
    stack = []		
    
    for i, v in enumerate(prices):
        while stack and stack[-1][1] > v:
            j = stack.pop()[0]
            answer[j] = i- j
        stack.append([i, v])
        
   # 끝까지 가격이 떨어지지 않은 애들
    while stack:
        i = stack.pop()[0]
        answer[i] = len(prices) - 1 - i
                
    return answer
