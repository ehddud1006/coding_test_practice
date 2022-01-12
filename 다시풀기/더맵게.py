import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7 
answer = 0
heapq.heapify(scoville)

key = False
while scoville[0] < K :
    if len(scoville) == 1 :
        key = True
        break
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    c = a+(b*2)
    heapq.heappush(scoville,c)
    answer += 1

if key :
    answer = -1   
    
print(answer)