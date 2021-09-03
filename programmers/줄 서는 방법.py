import math
def solution(n, k):
    answer = []
    nums = [i for i in range(1, n+1)]
        
    for i in range(n, 0, -1):
        fact = math.factorial(i-1) 
        # k = 0 ~ n-1, k가 n이 되면 잘못된 인덱스를 반환
        answer.append(nums.pop((k-1)//fact)) 
        k = k % fact
        print(i, ' ', k)
        
    return answer
