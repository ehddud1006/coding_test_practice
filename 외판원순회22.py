import sys

N = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
cost = [sys.maxsize]
visit = []
def backtracking(start,now,value) :
    visit.append(now)
    
    if value > cost[0]:
        return
    
    if len(visit) == N :
        if graph[now][start] != 0 :
            cost[0]= min(cost[0],value+graph[now][start])
        return 
    
    for i in range(N):
        if graph[now][i] != 0 and i not in visit :
            backtracking(start,i,value+graph[now][i])
            visit.pop()

backtracking(0,0,0)
print(*cost)