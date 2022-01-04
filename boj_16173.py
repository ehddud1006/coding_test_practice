from collections import deque

def bfs(x,y):

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        go = graph[x][y]

        for i in range(2):
            # 그래프에 적힌 수 만큼 이동
            nx = x + dx[i]*go
            ny = y + dy[i]*go
            
            # 구역 내부 제한
            if nx < 0 or ny < 0  or nx >=n or ny >=n :
                continue
            
            if visited[nx][ny] == False:
                visited[nx][ny] = True
                # print(visited)
                # print(f'{nx},{ny}')
                # f string 
                queue.append((nx,ny))
    # print(visited)
    if visited[n-1][n-1]==True :
        print("HaruHaru")
    else:
        print("Hing")


    
if __name__ == '__main__':
    n = int(input())

    graph = []
    visited = [[False] * n for _ in range(n)]

    # print(visited)
    for i in range(n):
        graph.append(list(map(int,input().split())))


    # 오른쪽방향 , 아래방향
    dx = [0,1]
    dy = [1,0]

    bfs(0,0)
        
