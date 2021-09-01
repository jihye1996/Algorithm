from collections import defaultdict


def solution(n, results):
    answer = 0
    win = defaultdict(set)
    lose = defaultdict(set)
    
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
        
    for i in range(1, n+1):    
        for l in win[i]:
            lose[l].update(lose[i])
        for w in lose[i]:
            win[w].update(win[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1: answer+=1
            
    return answer
