# from collections import deque
s = "}}}"
def check(target) :
    stack = []
    target = list(target)
    while len(target) :
        go = target.pop(0)
        if go == '[' or go == '(' or go == '{' :
            stack.append(go)
        elif len(stack)== 0 :
            stack.append(go)
        elif go == ']' and len(stack) > 0 :
            if stack[-1] == '[' :
                stack.pop() 
            else :
                stack.append(go)
        elif go == ')' and len(stack) > 0 :
            if stack[-1] == '(' :
                stack.pop() 
            else :
                stack.append(go)
        elif go == '}' and len(stack) > 0 :
            if stack[-1] == '{' :
                stack.pop()     
            else :
                stack.append(go)
    if len(stack) == 0 :
        return True
    else :
        return False            

def rotate(i,s) :
    for i in range(i):
        s = s[1:]+s[0]      
    return s          
    
def solution(s):
    answer = 0
    for i in range(len(s)) :
        target = rotate(i,s)
        if check(target) :
            answer +=1
    print(answer)
    return answer

solution(s)