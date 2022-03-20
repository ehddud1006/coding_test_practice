n=6
s=4
a=6
b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
def solution(n, s, a, b, fares):
    
    maxco =200 * 100000
    
    graph = [[maxco for row in range(n + 1)] for col in range(n+1)]
    
    for node in range(1,n+1):
        graph[node][node]=0
        
    for start,end,c in fares :
        graph[start][end]=c
        graph[end][start]=c
    
    # for i in range(n+1):
    #     print(graph[i])
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
    
    # for i in range(n+1):
    #     print(graph[i])
    
    answer=maxco
    
    for i in range(1,n+1):
        go = graph[s][i]+graph[i][a]+graph[i][b]
        answer = min(answer,go)
    
    return answer

solution(n, s, a, b, fares)