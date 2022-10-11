import sys
import heapq
input = sys.stdin.readline

num = int(input())

for i in range(num):
    maxh = []
    minh = []
    result = []
    count = 2
    caseN = int(input())
    caseNum = caseN // 10
    arr = []
    for i in range(caseNum+1) :
        arr.extend(list(map(int,input().split())))
    median = arr[0]
    heapq.heappush(maxh,-1*median)
    result.append(median)
    for i in range(1,len(arr)) :
        if count % 2 == 0:
            if arr[i] > -1*maxh[0] :
                heapq.heappush(minh,arr[i])
            else :
                heapq.heappush(minh,-1*heapq.heappop(maxh))
                heapq.heappush(maxh,-1*arr[i])

        else :
            if arr[i] > minh[0]:
                heapq.heappush(maxh,-1*heapq.heappop(minh))
                heapq.heappush(minh,arr[i])
            else:
                heapq.heappush(maxh,-1*arr[i])
            result.append(-1*maxh[0])
     
        count +=1
    print((caseN+1)//2)
    row = len(result) // 10
    answer=''
    for i in range(row):
        for j in range(10):
            answer += str(result[i*10+j])+" "
        answer+="\n"
    for i in range(row*10,len(result)) :
        answer += str(result[i])+" "
    print(answer)