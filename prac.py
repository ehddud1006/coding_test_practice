number = "1924"
k = 2

from collections import deque, defaultdict

def solution(number, k):
    num_cnt = defaultdict(int)
    choice_dq = deque()
    for i in range(k):
        num = number[i]
        num_cnt[num] += 1
        choice_dq.append(num)
    
    result = []
    i = k
    while i < len(number):
        num = number[i]
        num_cnt[num] += 1
        choice_dq.append(num)
        
        max_num = max(num_cnt.keys())
        result.append(str(max_num))
        while True:
            pn = choice_dq.popleft()
            num_cnt[pn] -=1
            if num_cnt[pn] == 0:
                num_cnt.pop(pn)
            if pn == max_num:
                break
        i += 1
        
    answer = ''.join(result)
    return answer

solution(number,k)