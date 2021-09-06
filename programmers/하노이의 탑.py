def hanoi(start, to, mid, n, answer):
    
    if n==1:
        return answer.append([start, to])
    
    # 1~n-1을 mid로 이동 + 마지막탑을 끝으로 이동 + 1~n-1탑을 mid에서 끝으로 이동
    # start, mid, to는 계속 바뀌기 때문에 변수로 처리
    hanoi(start, mid, to, n-1, answer)
    answer.append([start, to])
    hanoi(mid, to, start, n-1, answer)
    
def solution(n):
    answer = []
    hanoi(1, 3, 2, n, answer)
    return answer
