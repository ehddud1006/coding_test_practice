import sys
import heapq
input = sys.stdin.readline

maxh = []
minh = []

num = int(input())
first = int(input())
heapq.heappush(maxh,-1*first)
print(first)
for i in range(1,num) :
    target = int(input())
    if (i+1) % 2 == 0 :
        if -1*maxh[0] < target :
            heapq.heappush(minh,target)
        else :
            heapq.heappush(minh,-1*heapq.heappop(maxh))
            heapq.heappush(maxh,-1*target)
        # 출력
        print(-1*maxh[0])
    else :
        if minh[0] < target:
            heapq.heappush(maxh,-1*heapq.heappop(minh))
            heapq.heappush(minh,target)
        else :
            heapq.heappush(maxh,-1*target)
        # 출력
        print(-1*maxh[0])