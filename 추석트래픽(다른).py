import heapq
from typing import Tuple

lines = [
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

def solution(lines):
    answer = 0
    start_heap = []
    for log_str in lines:
        s, t = str_to_ms(log_str)                   # 문자열을 밀리초 단위의 정수로 변환
        heapq.heappush(start_heap, (s - t + 1, s))  # start_heap에 (시작 시간, 종료 시간)을 삽입한다
    
    end_heap = []
    while len(start_heap):                          # 새로운 로그가 시작될 때마다
        start, end = heapq.heappop(start_heap)
        heapq.heappush(end_heap, end)               # 시작된 로그의 종료 시간을 end_heap에 삽입한다
        while end_heap[0] <= start - 1000:          # end_heap에 있는 로그 중 현재 시점의 1초 전에 종료된 로그들을 모두 제거한다
            heapq.heappop(end_heap)
        answer = max(answer, len(end_heap))         # end_heap에 남아있는 로그의 개수를 계산하여 정답을 갱신한다
        
    return answer


def str_to_ms(log: str) -> Tuple[int, int]:
    date, s, t = log.split()
    hour, minute, sec = s.split(':')
    s_ms = int(1000 * float(sec)) + 1000 * (60 * int(minute) + 3600 * int(hour))
    t_ms = int(1000 * float(t[:-1]))
    return (s_ms, t_ms)

solution(lines)