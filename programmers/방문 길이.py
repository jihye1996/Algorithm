def solution(dirs):
    x, y = 0, 0
    moves = set([])
    for d in dirs:
        if d=="L" and (-5<=x-1 and x-1<=5):
            moves.add((x, y, x-1, y))
            moves.add((x-1, y, x, y))
            x-=1
        elif d=="R" and (-5<=x+1 and x+1<=5):
            moves.add((x, y, x+1, y))
            moves.add((x+1, y, x, y))
            x+=1
        elif d=="D" and (-5<=y-1 and y-1<=5):
            moves.add((x, y, x, y-1))
            moves.add((x, y-1, x, y))
            y-=1
        elif d=="U" and (-5<=y+1 and y+1<=5):
            moves.add((x, y, x, y+1))
            moves.add((x, y+1, x, y))
            y+=1
    
    return len(moves)/2
