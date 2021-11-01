import sys
from collections import deque
from collections import deque

def cal_candies(list_candy):
    result, cnt = 1, 1
    for i in range(len(list_candy)-1):
        if list_candy[i] == list_candy[i+1]:
            cnt += 1
        else:
            cnt = 1
        result = max(cnt, result)
    return result


input = sys.stdin.readline
N = int(input())
candy = []
answer = 0

for _ in range(N):
    candy.append(list(input())[:N])


for i in range(N):
    for j in range(N-1):
        #if candy[i][j] != candy[i][j+1]:
        # 좌우교환
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        # 영향 받은 열2개 및 행 1개 체크
        answer = max(answer, cal_candies(candy[i]))
        answer = max(answer, cal_candies(list(zip(*candy))[j]))
        answer = max(answer, cal_candies(list(zip(*candy))[j+1]))
        # 원위치
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        
        #if candy[j][i] != candy[j+1][i]:
        # 상하교환
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]
        # 영향 받은 행2개 및 열 1개 체크
        answer = max(answer, cal_candies(list(zip(*candy))[i]))
        answer = max(answer, cal_candies(candy[j]))             
        answer = max(answer, cal_candies(candy[j+1]))           
        # 원위치
        candy[j][i], candy[j+1][i] = candy[j+1][i], candy[j][i]

print(answer)
