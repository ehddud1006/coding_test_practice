import sys
from collections import deque
from typing import List

input = sys.stdin.readline


def solution() -> List[str]:
    res_list = []            # res_list: 정답을 담는 배열
    prefix_sums = [0]        # prefix_sums: 구간합을 담는 배열
    for idx, val in enumerate(num_list):
        prefix_sums.append(prefix_sums[-1] + val)
    while requests:     # requests: 입력받은 m개의 요청 구간(왼쪽, 오른쪽 인덱스)들을 담고 있는 덱
        l, r = requests.popleft()
        interval_sum = prefix_sums[r] - prefix_sums[l-1]
        res_list.append(str(interval_sum))
    return res_list


if __name__ == '__main__':
    n, m = map(int, input().split())
    num_list = list(map(int, input().split()))
    requests = deque([tuple(map(int, input().split())) for i in range(m)])
    sol = solution()
    print('\n'.join(sol))