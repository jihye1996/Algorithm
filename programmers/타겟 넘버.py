from itertools import product
def solution(numbers, target):
    data = [(i, -i) for i in numbers]
    result = list(map(sum, product(*data)))
    return result.count(target)

'''
retry 21.09.14
def solution(numbers, target):
    length = len(numbers)
    num_list = [[numbers[0], 0], [-1*numbers[0], 0]]
    answer = 0
    while 0 < len(num_list):
        v, i = num_list.pop()
        if i == length-1:
            if target == v:
                answer += 1
        else:
            num_list.append([v+numbers[i+1],i+1])
            num_list.append([v-numbers[i+1],i+1])
            
    return answer
'''
