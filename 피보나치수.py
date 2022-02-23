# import sys
# sys.setrecursionlimit(10**5)
# n=5

# def dfs(n):
#     if n == 0 :
#         return 0
#     if n == 1 :
#         return 1
#     return (dfs(n-1)+dfs(n-2)) % 1234567

# def solution(n):
#     print(dfs(10))
#     return 

# solution(n)

def solution(n):
    answer = 0
    fi =[]
    fi.append[0]
    fi.append[1]
    for i in range(2,n+1):
        fi[i] = fi[0]+fi[1] 
    
    return fi[n]%1234567