from collections import deque 
N = int(input())
M = int(input())

input = [list(map(int,input().split())) for _ in range(M)]

count = 0
queue = deque()
visited = [False] * (N+1)
graph = [ [] for _ in range(N+1) ]

for a,b in input :
    graph[a].append(b)
    graph[b].append(a)

visited[1] = True
queue.append(1)

while len(queue) > 0 : 
    v = queue.popleft()
    for i in range(len(graph[v])) :
        if not visited[graph[v][i]] :
            count += 1
            visited[graph[v][i]] = True
            queue.append(graph[v][i])

print(count)