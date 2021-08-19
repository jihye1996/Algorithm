from itertools import combinations
import collections
def solution(orders, course):
    answer = []
    for c in course:
        order_combs = []
        for order in orders:
            order_combs.extend(combinations(sorted(order), c))

        most_order = collections.Counter(order_combs).most_common() #return list
        #print(most_order)
        answer += [''.join(v) for v, c in most_order if 1 <  c and c == most_order[0][1]]
    return sorted(answer)
'''
from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        order_dicts = {}
        order_lists = []
        for order in orders:
            order_lists.extend(list(combinations(sorted(order), c)))
        
        for order in order_lists:
            strs = ''.join(order)
            if strs in order_dicts:
                order_dicts[strs] += 1
            else:
                order_dicts[strs] = 1

        if 0 < len(order_dicts) and 1 < max(order_dicts.values()):
            #print(order_dicts)
            answer += [order for order in order_dicts.keys() if order_dicts[order] == max(order_dicts.values())]
    return sorted(answer)
'''
