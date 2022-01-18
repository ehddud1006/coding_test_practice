import sys
from collections import deque

# visited = []

dx = [-1,-1,0,0,1,1]
dy = [-1,0,-1,1,0,-1]

W,H = map(int,input().split())

graph = [[] for _ in range(H)]
visited = [[False]*W for _ in range(H)]


def bfs(x,y):
    visited[x][y]=True
    q = deque()
    q.append((x,y))
    
    while q :
        a,b = q.appendleft()
        

for i in range(H):
    graph[i]=list(map(int,input().split()))

for i in range(H):
    print(graph[i])
   
for i in range(H):
    for j in range(W):
        if graph[i][j]==1 :
            bfs(i,j)
# print(visited[i])