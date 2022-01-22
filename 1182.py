import sys
from xml.dom import IndexSizeErr
input = sys.stdin.readline
N,S = map(int,input().split())
data = list(map(int,input().split()))
global count 
count = 0
sum = 0
def dfs(index,sum,sumcount) :
    print(f'index: {index} sum: {sum} sumcount: {sumcount}')
    global count 
    
    # 재귀마다 조건을 거는것을 확실하지 않으면 
    # 지양하자.
    # 다 끝나면 조건을 거는것이 베스트였다.
    
    if index >= N :
        if sum==S and sumcount>0:
            count+=1
        return 
    
    # if sum==S and sumcount>0:
    #     count+=1
    
    # if index >= N :
    #     print()
    #     return 
            
    dfs(index+1,sum,sumcount)
    dfs(index+1,sum+data[index],sumcount+1)
           
          

dfs(0,sum,0)
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