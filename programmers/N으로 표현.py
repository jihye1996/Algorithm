def solution(N, number):
    possible = [set() for i in range(9)]

    for i in range(1, 9):
        possible[i].add(int(str(N)*i)) # 5, 55, 555.. 자연수 추가
        for t in range(1, i//2+1): # 1 + N-1, 2 + N-2.. 케이스 확인
            for set_v1 in possible[t]: 
                for set_v2 in possible[i-t]:
                    possible[i].add(set_v1 + set_v2)
                    possible[i].add(set_v1 - set_v2)
                    possible[i].add(set_v2 - set_v1)
                    possible[i].add(set_v1 * set_v2)
                    if set_v1 != 0:
                        possible[i].add(set_v2 // set_v1)
                    if set_v2 != 0:
                        possible[i].add(set_v1 // set_v2)
        if number in possible[i]: 
            return i
    return -1
