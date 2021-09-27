from collections import Counter
from functools import reduce

def solution(clothes):
    counter = Counter(kind for name, kind in clothes) 
    answer = reduce(lambda x, y: x*(y+1), counter.values(), 1)
    return answer-1

'''
from collections import defaultdict

def solution(clothes):
    answer = 1
    dicts = defaultdict(int)
    
    for c, k in clothes:
        dicts[k] += 1
    lists = list(dicts.values())
    
    for i in lists:
        answer *= (i+1)

    return answer-1
'''
