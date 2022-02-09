from collections import deque
n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]

graph = [[] for _ in range(10)]
def bfs(x,visited) :
    q = deque()
    count = 0
    q.append(x)
    while len(q):
        count += 1
        v = q.popleft() 
        for i in graph[v]:
            if not visited[i] :
                q.append(i)
                visited[i]=True
    return count 
def solution(n, wires):
    answer = []
    
    for a,b in wires :
        graph[a].append(b)
        graph[b].append(a)
        
    for a,b in wires :
        visited = [False]*(n+1)
        visited[a]=True
        visited[b]=True
        ans1 = bfs(a,visited)
        ans2 = bfs(b,visited)
        answer.append(abs(ans1-ans2))
    
    print(min(answer))    
    return answer

solution(n,wires)