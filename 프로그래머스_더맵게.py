import heapq

scoville = [1, 2, 3, 9, 10, 12]
K = 7
heapq.heapify(scoville)

answer = 0

while scoville[0] < K and len(scoville)>1 :
    a = heapq.heappop(scoville)
    b = heapq.heappop(scoville)
    c = a + (b*2)
    heapq.heappush(scoville,c) 
    answer += 1

if scoville[0] < K :
    answer = -1
# while len(scoville)>1 :
#     if min(scoville)>=K :
#         break
#     else :
#         scoville.sort()
#         a= scoville.pop(0)
#         b =scoville.pop(1)
#         c = a + (b*b)
#         scoville.append(c)  
#         answer += 1

print(answer)