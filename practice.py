import sys
from collections import deque
input = sys.stdin.readline
# 문자열의 경우 realine을 사용하면 마지막의 개행문자까지 입력되므로
# rstrip()을 사용해서 제거해주어야한다.
enemy = input().rstrip()


ans = ''
tag = False

strr = deque()
for w in enemy :
    #1
    if w == " " and not tag:
        strr.append(" ")
        while len(strr) :
            ans += strr.popleft()
        # ans += strr + " "
        # strr =""
    #2
    elif w == "<" :
        tag = True
        while len(strr) :
            ans += strr.popleft()
        # ans += strr 
        strr.append('<')
        # strr = "<"
    #3
    elif w == ">" :
        tag = False
        strr.append(w)
        # strr = strr + w
        while len(strr) :
            ans += strr.popleft()
        # ans += strr 
        # strr = ""
        
    elif tag :
        strr.append(w)
        # strr = strr+w
    #6    
    else :
        strr.appendleft(w)
        # strr = w+strr

while len(strr) :
    ans += strr.popleft()        
# ans = ans + strr
print(ans)
    
    