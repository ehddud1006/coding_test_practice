import sys 
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
from collections import deque


# 이문제의 중요한 키워드 
# dic 을 통한 visited 효과 
# 참고한 자료 
# https://velog.io/@nyanyanyong/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EB%B0%B1%EC%A4%80-14867-%EB%AC%BC%ED%86%B5

a,b,c,d = map(int,input().split())
dic = {}
q = deque()
q.append((0,0))
dic[(0,0)] = 1
key = False
while q :
    i,j = q.popleft()
    
    if i == c and j == d :
        key = True
        break
    if (a,j) not in dic :
        q.append((a,j))
        dic[(a,j)] = dic[(i,j)] + 1
    
    if (0,j) not in dic :
        q.append((0,j))
        dic[(0,j)] = dic[(i,j)] + 1
        
    if (i,b) not in dic :
        q.append((i,b))
        dic[(i,b)] = dic[(i,j)] + 1
    
    if (i,0) not in dic :
        q.append((i,0))
        dic[(i,0)] = dic[(i,j)] + 1
    
    if i <= b-j :
        if (0,j+i) not in dic :
            q.append((0,j+i))
            dic[(0,j+i)] = dic[(i,j)] + 1
    else :
        if (i-(b-j),b) not in dic :
            q.append((i-(b-j),b))             
            dic[(i-(b-j),b)] = dic[(i,j)] + 1
    
    if  j <= a-i :
        if (i+j,0) not in dic :
            q.append((i+j,0))
            dic[(i+j,0)] = dic[(i,j)] + 1
    else :
        if (a,j-(a-i)) not in dic :
            q.append((a,j-(a-i)))
            dic[(a,j-(a-i))]=dic[(i,j)]+1

if key :          
    print(dic[(c,d)]-1)
else :
    print(-1)
    
    