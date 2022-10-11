import sys
import heapq
input = sys.stdin.readline

num = int(input())
heap = []
for i in range(num) :
    target= int(input())
    if target == 0 :
        if heap :
            ans = heapq.heappop(heap)
            print(ans[1])
        else :
            print(0)
    else :
        heapq.heappush(heap,(abs(target),target))
