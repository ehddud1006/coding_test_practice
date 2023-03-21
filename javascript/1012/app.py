from collections import deque
import sys
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())


for _ in range(T) :
    M, N, K = map(int,input().split())
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    count = 0 
    queue = deque()
    for i in range(K):
        a,b = map(int,input().split())
        graph[b][a] = 1
    
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and graph[i][j] == 1: 
                queue.append((i,j))
                count += 1

                while len(queue) > 0 :
                    x , y = queue.popleft()
                    visited[x][y] = True

                    for k in range(4) :
                        nx = x + dx[k]
                        ny = y + dy[k]
                        
                        if nx>-1 and nx <N and ny >-1 and ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                            visited[nx][ny] = True
                            queue.append((nx,ny))
                       

    print(count)

    
