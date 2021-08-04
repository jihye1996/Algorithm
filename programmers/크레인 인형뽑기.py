def solution(board, moves):
    stack = []
    ret = 0

    for value in moves:
        for i in range(0, len(board), 1):
            if board[i][value-1] != 0:
                if len(stack) == 0 or stack[-1] != board[i][value-1]:
                    stack.append(board[i][value-1])
                elif stack[-1] == board[i][value-1]:
                    del stack[-1]
                    ret+=2
                board[i][value-1] = 0
                break

    return ret
