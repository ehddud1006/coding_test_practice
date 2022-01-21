from collections import deque
from re import M
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def solution(maps):
    answer = -1
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0,0))
    while q :
        x,y = q.popleft()
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if xx<0 or yy<0 or xx>=n or yy>=m :
                continue
            if maps[xx][yy]==0 :
                continue
            if maps[xx][yy]== 1 :
                maps[xx][yy]=maps[x][y]+1
                if xx == n-1 and yy==m-1 :
                    answer = maps[xx][yy]
                q.append((xx,yy))
               
    print(answer)   
    return answer

solution(maps)