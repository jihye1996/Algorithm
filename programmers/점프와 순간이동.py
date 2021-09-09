def solution(n):
    ans = 0
    
    while 0 < n:
        ans += (n%2)
        n = n//2
    return ans
