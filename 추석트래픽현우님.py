lines =  [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
import heapq
def solution(lines):
    answer = 0
    
    period = []
    
    for line in lines:
        dtime = line[11:]
        ed_last = dtime.split(' ')
        ed = ed_last[0]
        last = float(ed_last[1][0:-1])
        sec = float(ed[0:2]) * 3600.0 + float(ed[3:5]) * 60.0 + float(ed[6:])
        
        period.append((sec-last+0.001, sec))
    
    period.sort(key=lambda t:t[0])
    
    pq = []
    
    for time in period:
        st = time[0]
        while(pq):
            if st - 1 >= pq[0][1][1]:
                heapq.heappop(pq)
            else:
                break
                
        heapq.heappush(pq, (time[1], time))
        answer = max(answer, len(pq))
    
    return answer

solution(lines)