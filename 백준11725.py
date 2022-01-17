
import sys
from collections import deque

sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for i in range(1,n):
    a,b = map(int,input().split())
    graph[a].append(b)   
    graph[b].append(a)
    


def bfs(v) :
    queue = deque()
    
    queue.append(v)
    
    visited[v] = True
    
    while queue :
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i] :
                queue.append(i)
                parents[i]=node
                visited[i]=True

bfs(1)

for i in range(2,n+1) :
    print(parents[i])

    
    