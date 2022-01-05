from collections import deque
n,m = map(int,input().split())

graph = []
visited = [[False]* m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int,input())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]    
    
print(graph)


def bfs (x,y):
    queue = deque()
    queue.append((x,y))
    visited[x][y]= True
        
    while queue :
        a ,b = queue.popleft()
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            
            if nx<0 or ny <0 or nx >= n or ny >= m :
                continue
            
            if graph[nx][ny] == 0:
                continue
            
            if not visited[nx][ny] :
                visited[nx][ny] = True
                graph[nx][ny]=graph[a][b]+1
                queue.append((nx,ny))

bfs(0,0)
for i in range(n):
    for j in range(m):
        print(f'{graph[i][j]} ',end=" ")
    print()  
print(graph[n-1][m-1])                