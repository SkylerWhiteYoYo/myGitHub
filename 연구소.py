import sys
import copy
input = sys.stdin.readline

N,M = map(int,input().strip().split())

map_start = []
for i in range(N):
    map_start.append(input().strip())
    
for i in range(N):
    
    print(map_start[i])

def spread_row(row):
    virus_index = []
    for i in range(len(row)):
        if row[i] == '2':
            virus_index.extend[i]
    print(virus_index)
spread_row('123452343123')
            
    
'''def spread_col():
    
def spread_virus(map_):
    previous_map = copy.deepcopy(map_)
    current_map = copy.deepcopy(map_)'''
    