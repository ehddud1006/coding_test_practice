
s = "cdcd"

def solution(s):
    answer = -1
    stack = []
    for c in s :
        if stack and stack[-1] == c:
            stack.pop()
        else :
            stack.append(c)
    if stack :
        answer =0
    else :
        answer = 1    
    
    return answer

a = solution(s)
print(a)