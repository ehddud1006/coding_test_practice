import sys
import heapq
input = sys.stdin.readline

num = int(input())
heap = []
for i in range(num):
    inputN = int(input())
    if inputN == 0 :
        if len(heap)==0:
            print(0)
        else :
            print(-1*heapq.heappop(heap))
    else :
        heapq.heappush(heap,-1*inputN)
    