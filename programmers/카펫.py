def solution(brown, yellow):
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            y = i
            x = yellow / i
            if brown - 4 == 2*(x+y):
                return [x+2, y+2]
