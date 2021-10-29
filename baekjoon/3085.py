import sys
from collections import deque
from collections import deque

# 수정하기
def cal_candies(list_candy):
    result, cnt = 1, 1
    for i in range(1,len(list_candy)):
        if list_candy[i] == list_candy[i-1]:
            cnt += 1
        else:
            cnt += 1
        result = max(cnt, result)
    return result


input = sys.stdin.readline
N = int(input())
candy = []
answer = 0

for _ in range(N):
    candy.append(list(input())[:N])

for i in range(N-1):
    for j in range(N-1):
        # 좌우교환
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        answer = max(answer, cal_candies(candy[i]))
        answer = max(answer, cal_candies(list(zip(*candy))[j]))
        answer = max(answer, cal_candies(list(zip(*candy))[j+1]))
        # 원위치
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        
        # 상하교환
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        answer = max(answer, cal_candies(candy[i]))
        answer = max(answer, cal_candies(candy[i+1]))
        answer = max(answer, cal_candies(list(zip(*candy))[j]))
        # 원위치
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

print(answer)
        
        


