import sys 
import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
from collections import deque

a,b,c,d = map(int,input().split())

# def bfs(depth,a,b,c,d):
#     if a==c and b==d :
#         print

q = deque()
q.append((0,0,0))

while q :
    
    depth,w,e = q.popleft()
    if depth == 9 :
        print("aa")
    if w==c and e==d :
        print(depth)
        break
    
    q.append((depth+1,a,e))
    q.append((depth+1,0,e))
    if w <= b-e :
        e = e+w
        w = 0
        q.append((depth+1,w,e))
    else :
        gap = b-e
        e = b
        w = w - gap
        q.append((depth+1,w,e))
    


    
    