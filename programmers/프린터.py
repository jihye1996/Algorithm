from collections import deque
def solution(priorities, location):
    answer = 0
    d = deque([(v, i) for i, v in enumerate(priorities)])

    while d:
        front = d.popleft()
        if d and max(d)[0] > front[0]:
            d.append(front)
        else:
            answer += 1
            if front[1] == location:
                break
    return answer
