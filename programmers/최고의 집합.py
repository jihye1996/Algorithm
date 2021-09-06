def solution(n, s):
    if s < n:
        return [-1]
    
    # 숫자 간격이 최소가 되는 값 찾기
    answer = [s//n] * n
    r = s%n
    
    # 끝 인덱스부터 +1씩
    for i in range(r):
        answer[-1-i] += 1
    
    return answer
