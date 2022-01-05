def dfs(graph,visited,v) :
    visited[v]=True
    print(f'{v} ',end=" ")
    
    for i in graph[v] :
        # print(i)
        if visited[i] == False :
            dfs(graph,visited,i) 

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

dfs(graph, visited, 1)
