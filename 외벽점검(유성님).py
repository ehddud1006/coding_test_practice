
# from itertools import permutations

n=12
weak =[1, 5, 6, 10]
dist = [1, 2, 3, 4]

from itertools import permutations
from collections import deque


def solution(n, weak, dist):
    answer = 0
    # num_friend = 2 라고 생각하고 디버깅
    for num_friend in range(1, len(dist) + 1):
        # order_case = (4,2)
        for order_case in permutations(dist, num_friend):
            # start를 기준으로 (1,5,6,10) (5,6,10,13) ... 원형으로 weak은 len만큼 덱에 넣는다.
            # (10,13,18,22)라고 생각하고 디버깅
            for start_idx in range(len(weak)):
                friend_dq = deque(order_case)
                weak_dq = deque(weak[start_idx:] + [x + n for x in weak[:start_idx]])
                while friend_dq and weak_dq:
                    # 검사할 수 있는 범위를 계산
                    end_pos = weak_dq.popleft() + friend_dq.popleft()
                    # 검사할 수 있는 범위보다 적다면 weak_dq를 pop 해준다.
                    while weak_dq and weak_dq[0] <= end_pos:
                        weak_dq.popleft()
                
                # while문을 다돌았을때 모든 벽을 점검했다면 num_friend를 리턴
                if not weak_dq:
                    return num_friend
    return -1

solution(n,weak,dist)
