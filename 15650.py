n,m = map(int,input().split())

# 백트레킹은 dfs로 조건을 주어서 구하는 것.
# 파이썬에서는 permutations를 사용가능함.

s=[]
def dfs(a):
    if len(s)==m:
        print(' '.join(s))
        return
    
    for i in range(a,n+1):
        if str(i) not in s:
            s.append(str(i))
            dfs(i+1)
            s.pop()

dfs(1)