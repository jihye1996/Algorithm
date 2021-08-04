def solution(absolutes, signs):
    
    
    for i, v in enumerate(signs):
        if v == False:
            absolutes[i]*=-1
            
    return sum(absolutes)
