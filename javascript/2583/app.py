
import sys
sys.setrecursionlimit(100000)
N, M ,K = map(int,input().split(' '))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

graph = [[0] * M for _ in range(N) ]
size,answer = 0,0
sizeArr = []

def dfs(i, j) :
    global size
    if  i <= -1 or i >= N or j <= -1 or j >= M or graph[i][j] == 1: 
        return 
    
    graph[i][j] = 1
    size += 1

    for k in range(4) :
        ni,nj = i + dx[k], j + dy[k]
        dfs(ni,nj)
    



for _ in range(K) : 
    leftBottomCol, leftBottomRow, rigthTopCol, rightTopRow = map(int,input().split(' '))

    for i in range( N - rightTopRow,  N  - leftBottomRow) :
        for j in range(leftBottomCol,rigthTopCol) :
            graph[i][j] = 1

for i in range(N) :
    for j in range(M):
        if graph[i][j] == 0 :
            size = 0
            answer += 1
            dfs(i,j)
            sizeArr.append(size)

print(answer)
sizeArr.sort()
print(' '.join(map(str,sizeArr)))