def solution(n, times):
    answer = 0
    right = n * max(times)
    left = 1
    
    while left < right:
        mid = (left + right) // 2
        people = 0
        for t in times:
            people += mid // t
            if n <= people:
                break
        
        if n <= people:
            right = mid
        else:
            left = mid + 1 
        answer = left
    
    return answer
