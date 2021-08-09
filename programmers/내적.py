def solution(a, b):
    #zip 내장함수 속도가 더 빠름
    return sum([x*y for x,y in zip(a,b)])
