import heapq
import sys
testDataNumber = int(input())
# 우선순위 큐 = heap
# 이중 우선순위 큐 = maxheapq , minheapq 를 visit 배열을 사용해서 서로 연결한 것.
# heapq 의 디폴트는 최소힙 따라서 최대힙을 구현하기 위해서는 value에 -1 값을 넣어주므로써 구현이 가능
strr = ''
for i in range(testDataNumber) :
    maxhq = []
    minhq = []
    expressionNumber = int(input())
    done = [False]* expressionNumber
    for j in range(expressionNumber):
        # print(j)
        a,b = sys.stdin.readline().strip().split(" ")
        # print(a,b)
        if a == 'I' :
            heapq.heappush(maxhq,((-1)*int(b),j))
            heapq.heappush(minhq, (int(b),j))          
        if a == "D" :
            if b == '-1':
                while minhq :
                    if done[minhq[0][1]] :
                        heapq.heappop(minhq)
                    else :
                        if minhq :
                            minn = heapq.heappop(minhq)
                            done[minn[1]] = True
                        break
            elif b == '1':
                while maxhq :
                    if done[maxhq[0][1]] :
                        heapq.heappop(maxhq)
                    else :
                        if maxhq :
                            maxx = heapq.heappop(maxhq)
                            done[maxx[1]] = True
                        break
    while minhq :
        if done[minhq[0][1]] :
            heapq.heappop(minhq)
        else :
            break
    while maxhq :
        if done[maxhq[0][1]] :
            heapq.heappop(maxhq)
        else :
            break
    if minhq :
        strr += f'{-1* maxhq[0][0]} {minhq[0][0]}\n'
    else :
        strr += 'EMPTY\n'

print(strr)
