import copy
n = int(input())
board = []
for i in range(n):
    board.append('.'*n)
    
def num_to_xy(num):
    x = num % n
    y = num // n
    return x,y

def put_queen(num):
    global board
    x,y = num_to_xy(num)
    board[y] = board[y][:x] + "Q" + board[y][x+1:] 
    
def del_queen(num):
    global board
    x,y = num_to_xy(num)
    board[y] = board[y][:x] + "." + board[y][x+1:]
    
def print_b():
    for i in range(n):
        print(board[i])
    print()
             
can_put = [True] * n*n
visited = [False] * n*n
def del_row(y,can_put):
    for i in range(n):
        can_put[n*y+i] = False
def del_col(x,can_put):
    for i in range(n):
        can_put[x+i*n] = False   
def del_diagonal(x,y,can_put):
    for i in range(n):
        if x+i < n and y+i < n:
            can_put[(y+i)*n+x+i] = False
        if x+i < n and y-i >= 0 :
            can_put[(y-i)*n+(x+i)]=False
        if x-i >= 0 and y+i < n:
            can_put[(y+i)*n+(x-i)] = False
        if x-i >= 0 and y-i >= 0 :
            can_put[(y-i)*n+(x-i)]=False


def del_queen_path(num,can_put):
    x,y=num_to_xy(num)
    del_row(y,can_put)
    del_col(x,can_put)
    del_diagonal(x,y,can_put)
    
def count_queen():
    global board
    count = 0
    for i in board:
        for k in range(n):
            if i[k] == 'Q':    
                count += 1
    return count

def refresh_can_put():
    can_put = [True]*n*n
    for i in range(n*n):
        if board[i//n][i%n] == 'Q':
            del_queen_path(i)
    print(can_put)
            
count_cleared = 0

def dfs(num,can_put,count):
    global count_cleared
    print_b()
    if num<0 or num > n*n or not can_put[num]:
        return
    if count == n:
        count_cleared += 1
        return
    
    put_queen(num)
    can_put_copy = can_put.copy()
    del_queen_path(num, can_put)

    
    possibles = [i for i in range(len(can_put)) if can_put[i] == True]
    if not possibles:
        del_queen(num)
        can_put[:] = can_put_copy
        return
    
    for i in possibles:
        dfs(i,can_put,count+1)

    can_put[:] = can_put_copy
    del_queen(num)

    
    
dfs(0,can_put,1)    

print(count_cleared)
   
    
