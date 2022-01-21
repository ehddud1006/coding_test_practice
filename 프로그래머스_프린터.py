from collections import deque

priorities = [2, 1, 3, 2]
location = 2

def solution(priorities, location):
    real_priorities = priorities[:]
    real_priorities.sort(reverse=True)
    print(priorities)
    print(real_priorities)
    # real_priorities.pop(0)
    q = deque()
    index = 0
    while priorities :
        if location == index :
            q.append((priorities.pop(0),1))
        else:
            q.append((priorities.pop(0),0))
        index +=1
    count = 0
    ans = 0
    while real_priorities :
        p = real_priorities.pop(0)
        while True :
            a , b = q.popleft()
            if p == a :
                count +=1
                if b == 1 :
                    ans = count
                break
            else :
                q.append((a,b))
    print(ans)
    return ans

solution(priorities,location)