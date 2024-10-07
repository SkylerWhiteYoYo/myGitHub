import copy
ms = [[1,2,3,4],[8,7,6,5]]
s = list(map(int,input().split()))
target = []
target.append([s[0],s[1],s[2],s[3]])
target.append([s[7],s[6],s[5],s[4]])

def trans(magic_square,way) :
    ms_new = copy.deepcopy(magic_square)
    if way == 0:#윗줄 아랫줄 교체
        temp = copy.deepcopy(ms_new[0])
        ms_new[0] = copy.deepcopy(ms_new[1])
        ms_new[1] = copy.deepcopy(temp)
        return(ms_new)
    elif way == 1:#각줄 오른쪽으로 밀기
        temp1,temp2 = ms_new[0][3],ms_new[1][3]
        ms_new[0][3] = ms_new[0][2]
        ms_new[0][2] = ms_new[0][1]
        ms_new[0][1] = ms_new[0][0]
        ms_new[0][0] = temp1
        ms_new[1][3] = ms_new[1][2]
        ms_new[1][2] = ms_new[1][1]
        ms_new[1][1] = ms_new[1][0]
        ms_new[1][0] = temp2
        return(ms_new)
    elif way == 2:# 가운데 4개 반시계
        temp = ms_new[0][1]
        ms_new[0][1] = ms_new[0][2]
        ms_new[0][2] = ms_new[1][2]
        ms_new[1][2] = ms_new[1][1]
        ms_new[1][1] = temp 
        return(ms_new)
    elif way == 3:# 1번위치와 5번위치 변환
        temp = ms_new[0][0]
        ms_new[0][0] = ms_new[1][3]
        ms_new[1][3] = temp
        return(ms_new)

lvl = 0
def do_ways(magic_square,lvl):
    maps =[]
    for i in range(4):
        ms_new = copy.deepcopy(magic_square)
        maps.append(trans(ms_new,i))
    print(map_square)
    
map_square = []
map_square.append([])
flag = False
while not flag:
    
 

