from configparser import ConfigParser


n=3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

def dfs(graph,v,visit) :
    visit[v]=True
    for w in graph[v]:
        if not visit[w]:
            dfs(graph,w,visit)
    return 1
def solution(n, computers):
    answer = 0
    graph = [[]*n for _ in range(n)]
    visit = [False]*n
    for i in range(n):
        for j in range(n):
            if computers[i][j]==1 :
                graph[i].append(j)
    for i in range(n):
        if not visit[i] :
            answer+=dfs(graph,i,visit)
    
                
                
    return answer

solution(n,computers)