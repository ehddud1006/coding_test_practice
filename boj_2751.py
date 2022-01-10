import sys
import heapq

input = sys.stdin.readline
heap = [] 

n=int(input())

# list =[]
# for i in range(n):
#     a=int(input())
#     list.append(a)
    
# list.sort()

# for i in range(n):
#     print(list[i])    

for i in range(n):
    heapq.heappush(heap,int(input()))
    
for i in range(n):
    print(heapq.heappop(heap))  