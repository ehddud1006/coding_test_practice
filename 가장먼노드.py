from collections import deque
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
graph = [[] for i in range(n+1) ]
visit = [False] * (n+1)
ans = [0]*(n+1)
def bfs(v) :
  visit[v]=True
  q = deque()
  q.append((v,0))

  while len(q) != 0 :
    a , d = q.popleft()

    for i in graph[a]: 
      if not visit[i] :
        q.append((i,d+1))
        visit[i]=True
        ans[i] = d+1 

  
    
   
for tex in vertex :
  graph[tex[0]].append(tex[1])
  graph[tex[1]].append(tex[0])

# print(graph)

bfs(1)
m = max(ans)
count = 0
for i in range(len(ans)):
  if ans[i] == m :
    count+=1

# print(count)