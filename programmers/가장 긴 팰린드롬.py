def solution(s):
    # s는 자연수이므로 최소 1
    answer = 1 
    
    for i in range(2, len(s)+1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1] and answer < len(s[j:j+i]):
                answer = len(s[j:j+i])
    return answer
