import sys
sys.setrecursionlimit(100000)
def dfs(x,y):
    if x<0 or y<0 or x>=n or y>=m :
        return False
    
    if graph[x][y]==1:
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    
    return False
                 

T = int(input())

for i in range(T) :
    m,n,k = map(int,input().split())
    graph = [[0]*m for _ in range(n)]
    # for p in range(n):
    #     for o in range(m):
    #         print(f'{graph[p][o]}', end=" ")
    #     print()    
    # print(graph)
    for j in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
        
    # for p in range(n):
    #     for o in range(m):
    #         print(f'{graph[p][o]}', end=" ")
    #     print()    
        
    result = 0    
    for p in range(n):
        for o in range(m):   
            if dfs(p,o):
                result+=1
                
    print(result)            
                
                
    
   
        