import sys
from typing import Tuple


input = sys.stdin.readline
MAX_ABS_SUM = 3_000_000_001


def solution() -> Tuple[int, int, int]:
    num_list.sort()
    min_abs_sum = MAX_ABS_SUM
    for lp in range(n - 2):
        mp, rp = lp + 1, n - 1
        while mp < rp:
            cur_sum = num_list[lp] + num_list[mp] + num_list[rp]
            cur_abs_sum = abs(cur_sum)
            if cur_abs_sum < min_abs_sum:
                min_abs_sum = cur_abs_sum
                best_mix = (num_list[lp], num_list[mp], num_list[rp])
                if min_abs_sum == 0:        # 세 용액의 특성값이 0인 경우
                    return best_mix         # 더 이상의 탐색 없이 최적의 조합을 리턴한다

            if cur_sum > 0:                 # 세 용액의 특성값이 양수인 경우
                rp -= 1                     # 오른쪽 포인터를 한 칸 왼쪽으로 움직인다
            else:                           # 세 용액의 특성값이 음수인 경우
                mp += 1                     # 중간 포인터를 한 칸 오른쪽으로 움직인다

    return best_mix


if __name__ == '__main__':
    n = int(input())
    num_list = list(map(int, input().split()))

    print(*solution())