s = "abcdcba"
from collections import deque
def solution(s):
    answer = 0
    odd_even = deque()
    for i in range(len(s)):
        odd_even.append((i,i))
        odd_even.append((i,i+1))
        while len(odd_even) != 0 :
            lp , rp = odd_even.popleft()
            cnt = 0
            while 0<=lp and rp <= len(s)-1 :
                if lp == rp  :
                    cnt +=1
                    lp -= 1
                    rp += 1
                elif s[lp] == s[rp] :
                    cnt+=2
                    lp -= 1
                    rp +=1 
                else :
                    break
            answer = max(answer, cnt)
    return answer

solution(s)