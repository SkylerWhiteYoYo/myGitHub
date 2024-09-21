import sys
input = sys.stdin.readline
dir = 'E'
N = int(input().strip())
K = int(input().strip())
apple_loc = []
for i in range(K):
    x,y = map(int,input().strip().split())
    z = [x,y]
    apple_loc.append(z)

L = int(input().strip())
for i in range(L):
    X,C = input().strip().split()
    X = int(X)

def make_board(N):
    board = []
    line = '.'*N
    for i in range(N):
        board.append(line)
    return board
def add_apple_board(board,x,y):
    board[x-1] = board[x-1][:y-1] + 'A' + board[x-1][y:]
    return board


board = make_board(N)
print(apple_loc)
for i in range(K):
    board = add_apple_board(board,*apple_loc[i])
    print(*apple_loc[i])
print(board)

cur_dir = 0


tick = 0