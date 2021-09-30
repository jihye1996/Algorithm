def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


'''
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer

def solution(citations):
    citations.sort(reverse=True)
    count = [(0,0)]
    for i in range(max(citations), -1, -1):
        count.append((i, citations.count(i) + count[len(count)-1][1]))

    for x, y in count[1:]:
        if x <= y: return x
    return 1
'''
