from itertools import combinations

def solution(nums):
    answer = 0
    List = list(combinations(nums,3))
    
    for i in List:
        flag = check(sum(i))
        if flag == True:
            answer+=1
    return answer

def check(num):
    if num % 2 == 0:
        return False
    
    for i in range(3, num, 2):
        if num % i == 0:
            return False
        
    return True
