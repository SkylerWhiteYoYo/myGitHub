import sys
import copy
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
TD_info = []
for i in range(L):
    X,C = input().strip().split()
    X = int(X)
    TD_info.append([X,C])

is_game_running = True
def make_board(N):
    board = []
    line = '.'*N
    for i in range(N):
        board.append(line)
    return board
def add_apple_board(board,x,y):
    board[x-1] = board[x-1][:y-1] + 'A' + board[x-1][y:]
    return board
    


#보드와 사과 생성
board = make_board(N)
for i in range(K):
    board = add_apple_board(board,*apple_loc[i])

def change_thing(row,col,thing):
    board[row-1] = board[row-1][:col-1] + thing + board[row-1][col:]
def return_head_loc():
    for i in range(len(board)):
        if 'H' in board[i]:
            row = i+1
            col = board[i].index('H') + 1
            return row,col
cur_dir = 0
len_tail = 0
remove_tail_array = []
def track_tail():
    global remove_tail_array
    global tick
    global len_tail
    x,y = return_head_loc
    remove_tail_array.append([tick+len_tail,x,y])
def remove_tail_by_tick():
    global tick
    global remove_tail_array
    for i in range(len(remove_tail_array)):
        if tick == remove_tail_array[i][0]:
            x = remove_tail_array[i][1]
            y = remove_tail_array[i][2]
            change_thing(x,y,'.')
        
       
    
def print_board(board):
    for i in range(N):
        print(board[i])
def move_head():
    global cur_dir
    global len_tail
    global is_game_running
    row,col = map(int,return_head_loc())
    pre_row = copy.deepcopy(row)
    pre_col = copy.deepcopy(col)
    
    if cur_dir == 0:
        col += 1
    elif cur_dir == 1:
        row += 1
    elif cur_dir == 2:
        col -= 1
    elif cur_dir == 3:
        row -= 1
    elif cur_dir == 4:
        col += 1
        cur_dir = 0
    elif cur_dir == -1:
        row -= 1
        cur_dir = 3
        
    if col < 1 or col > N :
        print("범위를 벗어남")
        is_game_running = False
        return
    if row < 1 or row > N :
        print("범위를 벗어남")
        is_game_running = False
        return
    if board[row-1][col-1] == 'S':
        print("몸에 부딪힘")
        is_game_running = False
        return
    if board[row-1][col-1] == 'A':
        len_tail += 1
        print('사과를 먹음')
    
    change_thing(row,col,'H')

    if len_tail > 0:
        change_thing(pre_row,pre_col,'S')
        remove_tail(return_head_loc)
    elif len_tail == 0:
        change_thing(pre_row,pre_col,'.')
   
tick = 0
change_thing(1,1,'H')
while is_game_running:
    print(TD_info)
    for i in range(len(TD_info)):
        if TD_info[i][0] == tick:
            print("방향을 바꿈",TD_info[i][1])
            if TD_info[i][1] =='L':
                cur_dir -= 1
            elif TD_info[i][1] =='D':
                cur_dir += 1
    #TODO:지나간 틱은 지워야함 
    move_head()
    
    tick +=1
    print_board(board)
    print()