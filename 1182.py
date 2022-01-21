import sys
input = sys.stdin.readline
N,S = map(int,input().split())
data = list(map(int,input().split()))
global count 
count = 0
arr = []
visit = [False]*N
def dfs(a,visit) :
    global count 
    if sum(arr)==S and arr:
        count+=1
    for i in range(a,len(data)):
        if not visit[i]:
            visit[i]=True
            arr.append(data[i])
            dfs(i+1,visit)
            arr.pop()
            visit[i]=False

dfs(0,visit)
print(count)
# def dfs(i,limit,l) :
#     global count
#     if sum(arr)==S and limit!=0 :
#         count +=1
#     if limit == l :
#         return
#     arr.append(data[i])
#     dfs(i+1,limit+1,l)
#     arr.pop()

# for i in range(len(data)):
#     dfs(i,0,len(data)-i)
# print(count)




# from sys import stdin

# N,S=map(int,stdin.readline().split())
# n_list=list(map(int,stdin.readline().split()))
# cnt=0


# def back(idx,sub_sum):
#     global cnt
    
#     if idx==N:
#         return
    
#     sub_sum+=n_list[idx]
    
#     if sub_sum==S:
#         cnt+=1
#     back(idx+1,sub_sum)
#     back(idx+1,sub_sum-n_list[idx])
        
# back(0,0)
# print(cnt)