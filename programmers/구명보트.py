def solution(people, limit):
    
    people.sort()
    answer = len(people)
    i, j = 0, len(people)-1
    
    while i<j:
        if people[i]+people[j]<=limit:
            answer-=1
            i+=1
        j-=1
    return answer
