from collections import deque

N = int(input())

graph = []
visited = [[False] * N for _ in range(N)]

for i in range(N):
    graph.append(list(map(int,input().split())))

# print(graph)

dx = [0,1]
dy = [1,0]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    # print(queue)
    while queue:
        x, y = queue.popleft()
        go = graph[x][y]
        
        for i in range(2):
            nx = x + dx[i]*go
            ny = y + dy[i]*go
            
            if nx<0 or ny<0 or nx>=N or ny>=N :
                continue
            
            if visited[nx][ny]==False :
                queue.append((nx,ny))
                visited[nx][ny]= True
    
    if visited[N-1][N-1] == True :
        print("HaruHaru")
    else:
        print("Hing")           
        
bfs(0,0)
