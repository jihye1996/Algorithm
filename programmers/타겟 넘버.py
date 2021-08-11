from itertools import product
def solution(numbers, target):
    data = [(i, -i) for i in numbers]
    result = list(map(sum, product(*data)))
    return result.count(target)
