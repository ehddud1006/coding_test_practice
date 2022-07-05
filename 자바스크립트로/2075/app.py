import sys
import heapq
input = sys.stdin.readline

num = int(input())
heap = []
for i in range(num):
    arr = list(map(int,input().split()))
    if i == 0 :
        heap = arr[:]
        heapq.heapify(heap)
    else :
        for j in range(num):
            if heap[0] < arr[j] :           
                heapq.heappop(heap)
                heapq.heappush(heap,arr[j])

print(heap[0])