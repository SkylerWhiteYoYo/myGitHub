def board(N):
    board = []
    line = '.'*N
    for i in range(N):
        board.append(line)
    return board
    
print(board(3))