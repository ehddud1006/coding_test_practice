N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

s = []
visit = [False]*N
def dfs() :
    fobidden = []
    if len(s) == M :
        print(' '.join(s)) 
        return 
    for i in range(N):
        if not visit[i] and arr[i] not in fobidden:
            visit[i] = True
            fobidden.append(arr[i])
            s.append(str(arr[i]))
            dfs()
            s.pop()
            visit[i] = False
    return
        
dfs()            
