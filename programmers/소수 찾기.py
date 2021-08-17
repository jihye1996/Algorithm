import math
from itertools import permutations
def solution(numbers):
    answer = set()
    
    for i in range(1, len(numbers)+1):
        array = list(map(''.join, permutations(numbers, i)))
        for i in array:
            if find(int(i)) == True and int(i) not in (0, 1):
                answer.add(int(i))
    print(answer)
    return len(answer)

def find(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
