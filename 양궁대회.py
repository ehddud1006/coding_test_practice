n=5
info = [2,1,1,1,0,0,0,0,0,0,0]
ans = [0]*11
num = [-9999999]
def dfs(limit) :
    if limit == n :
        ryan = 0
        appeach = 0
        for i in range(11):
            if info[i]>= ans[i]:
                appeach += 10-i
            else :
                ryan += 10-i
        if num[0]<ryan-appeach:
            num[0]=ryan-appeach
    for i in range(0,11) :
        ans[i]+=1
        dfs(limit+1)
        ans[i]-=1

def solution(n, info):
    answer = []
    dfs(0)
    print(*num)
    return answer

solution(n,info)