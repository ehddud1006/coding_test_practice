n,m = map(int,input().split())
su = list(map(int,input().split()))
su.sort()
# 백트레킹은 dfs로 조건을 주어서 구하는 것.
# 파이썬에서는 permutations를 사용가능함.

s=[]
visit = [False]*n
def dfs(visit):
    fobidden = []
    if len(s)==m:
        print(' '.join(s))
        return
    
    for i in range(0,n):
        if  su[i] not in fobidden:
            visit[i]=True
            fobidden.append(su[i])
            s.append(str(su[i]))
            dfs(visit)
            s.pop()
            visit[i]=False
dfs(visit)