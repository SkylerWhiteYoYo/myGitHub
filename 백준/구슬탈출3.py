import sys
import copy
input = sys.stdin.readline
N,M = map(int,input().strip().split())
map = []
for i in range(N):
    map.append(input().strip())

def getLD(ball_color,direction,map): #공색과, 방향을 받아 이동시킬 방향의 공이있는 라인을 불러오는 역할
    if direction == 'u' or direction == 'd':
        for i in map:
            if ball_color in i:
                column_ball = i.index(ball_color)
        map_column = ''.join([map[i][column_ball] for i in range(len(map))])
        return map_column,direction

    elif direction == 'l' or direction == 'r':
        for i in range(len(map)):
            if ball_color in map[i]:
                currentLine = map[i]
                
                return currentLine,direction
    return '',''

def slide_ball(line,direction):
    if direction == 'd' or direction == 'r':
        line = line[::-1]
    
    for k in range(len(line)-3):
        for i in range(2,len(line)-1):
            if line[i] == '#' or line[i] == '.' or line[i] == 'O':
                continue
            elif line[i] =='B' or line[i] == 'R':
                if line[i-1] == '#':
                    continue
                elif line[i-1] == 'O' :
                    line = line[:i] + '.' + line[i+1:]
                elif line[i-1] == '.':
                    line = line[:i-1] + line[i] + line[i:]
                    line = line[:i] + '.' + line[i+1:]
                elif line[i-1] == 'B' or line[i-1] == 'R':
                    continue
    if direction == 'd' or direction == 'r':
        line = line[::-1]    
    
    return line            

def executeMoves(direction,map): #콜무브가 준 Line과 Direction을 이용해서 수정사항을 현상황에 반영시켜야함
    changed_map = copy.deepcopy(map)
    LineB =slide_ball(*getLD('B',direction,changed_map))
    LineR =slide_ball(*getLD('R',direction,changed_map))
    if direction == 'u' or direction == 'd':
        for i in range(len(changed_map)):
            if 'B' in changed_map[i]:
                indexB = changed_map[i].index('B')
                for k in range(len(changed_map)):
                    changed_map[k] = changed_map[k][:indexB] + LineB[k] + changed_map[k][indexB+1:]
        

                
        for i in range(len(changed_map)):
            if 'R' in changed_map[i]:
                indexR = changed_map[i].index('R')
                for k in range(len(changed_map)):
                    changed_map[k] = changed_map[k][:indexR] + LineR[k] + changed_map[k][indexR+1:]
        
        
        return changed_map

            
            
    elif direction == 'l' or direction == 'r':
        for i in range(len(changed_map)):
            if 'B' in changed_map[i]:
                changed_map[i] = LineB
                
        for i in range(len(changed_map)):
            if 'R' in changed_map[i]:
                changed_map[i] = LineR
        return changed_map          

def findPossibleCases(map):
    possibleCase = []
    currentlineB,_ = getLD('B','l',map)
    currentlineR,_ = getLD('R','l',map)
    
    if currentlineB == '' or currentlineR == '':
        return []
    
    indexR = currentlineR.index('R')
    indexB = currentlineB.index('B')
    if currentlineB[indexB-1] == '.' or currentlineR[indexR-1] == '.':
        possibleCase.append('l')
    if currentlineB[indexB+1] == '.' or currentlineR[indexR+1] == '.':
        possibleCase.append('r')
        
    if currentlineR[indexR-1] == 'O':
        possibleCase = 'l'
        return possibleCase
    if currentlineR[indexR+1] == 'O':
        possibleCase = 'r'
        return possibleCase
    
    currentlineB,_ = getLD('B','u',map)
    currentlineR,_ = getLD('R','u',map)
    indexR = currentlineR.index('R')
    indexB = currentlineB.index('B')
    if currentlineB[indexB-1] == '.' or currentlineR[indexR-1] == '.':
        possibleCase.append('u')
    if currentlineB[indexB+1] == '.' or currentlineR[indexR+1] == '.':
        possibleCase.append('d')
    
    if currentlineR[indexR-1] == 'O':
        possibleCase = 'u'
        return possibleCase
    if currentlineR[indexR+1] == 'O':
        possibleCase = 'd'
        return possibleCase
    
    return possibleCase

def examine_success(map):
    existR = False
    existB = False
    code = 'RB'
    for i in map:
        if 'R' in i:
            existR = True
        if 'B' in i:
            existB = True
    if existR == True and existB == False:
        code = 'Rx'
    if existR == False and existB == False:
        code = 'xx'
    if existR == False and existB == True:
        code = 'xB'
    return code
        
#맵 하나를 주면 가능한 방향찾고, 시도한 결과 맵들을 돌려줘야함 그리고 그 결과에 대해서 결과 배열도 주면 좋을듯
def result_maps_examines(map):
    examines = []
    maps = [] 
    possible_case = findPossibleCases(map)
    if possible_case == []:
        return [],[]
    for i in range(len(possible_case)):
        current_map = executeMoves(possible_case[i],map)
        maps.append(current_map)
        examines.append(examine_success(current_map))
    return maps, examines    

def return_map_if_absent(map,level):
    for i in range(level):
        for k in range(len(maps[i])):
            if  maps[i][k] == map :
               return []
    return map


flag = False
level = 0
maps = []
for i in range(11):
    maps.append([])
maps[0] = []
maps[0].append(copy.deepcopy(map))
#print(maps)
while True:
    if level > 9 :
        print(-1)
        break

    for i in range(len(maps[level])):
        map_checked = return_map_if_absent(maps[level][i],level)
        maps_to_append,examines = result_maps_examines(map_checked)
        if maps_to_append != None:
            maps[level+1].extend(maps_to_append)
        #print(maps,"i:",i)
        #print(examines)
        #print("level :",level+1)
        
        if isinstance(examines,list) and 'xB' in examines: #이게 문제인거같은데
            flag = True
            break  
    if flag == True:
        #print('성공')
        print(level+1)
        break
    print(maps)
    level += 1 
