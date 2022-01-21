from sys import stdin

N,S=map(int,stdin.readline().split())
n_list=list(map(int,stdin.readline().split()))
cnt=0


def back(idx,sub_sum):
    global cnt
    
    if idx==N:
        return
    
    sub_sum+=n_list[idx]
    
    if sub_sum==S:
        cnt+=1
    back(idx+1,sub_sum)
    back(idx+1,sub_sum-n_list[idx])
        
back(0,0)
print(cnt)