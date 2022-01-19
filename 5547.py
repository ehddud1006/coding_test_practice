import sys
from collections import deque

# visited = []

# 풀이참고 
# https://reliablecho-programming.tistory.com/110

dx = [-1,-1,0,0,1,1]
dy = [[-1,0,-1,1,-1,0],[0,1,-1,1,0,1]]
        # 짝

W,H = map(int,input().split())

graph_extra = [[0]*(W+2) for _ in range(H+2)]
visited = [[False]*(W+2) for _ in range(H+2)]

graph = [[] for _ in range(H)]

for i in range(H):
    graph[i]=list(map(int,input().split()))

# for i in range(H):
#     print(graph[i])

for i in range(1,H+1):
    for j in range(1,W+1):
        graph_extra[i][j]=graph[i-1][j-1]

# for i in range(H+2):
#     print(graph_extra[i])

q = deque()
q.append((0,0))
count = 0
while q :
    x,y = q.popleft()
    visited[x][y]=True
    
    if x%2==1 :
        for i in range(6): 
            xx = x+dx[i]
            yy = y+dy[1][i]

            if xx<0 or yy<0 or xx >= H+2 or yy >=W+2 :
                continue
            
            if graph_extra[xx][yy]==1:
                count +=1
            
            if graph_extra[xx][yy]==0 and not visited[xx][yy] :
                visited[xx][yy] = True
                q.append((xx,yy))
                
    elif x%2==0 :
        for i in range(6): 
            xx = x+dx[i]
            yy = y+dy[0][i]

            if xx<0 or yy<0 or xx >= H+2 or yy >=W+2 :
                continue
            
            if graph_extra[xx][yy]==1:
                count +=1
            
            if graph_extra[xx][yy]==0 and not visited[xx][yy] :
                visited[xx][yy] = True
                q.append((xx,yy))
            

print(count)