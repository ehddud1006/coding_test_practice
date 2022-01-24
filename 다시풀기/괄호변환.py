# slice 할때 , p = ")(" 이고  w = p[2:] 이렇게 slice 해도
# 에러가 나지않고 w = "" 가 저장된다. 킹 갓 언어 파이썬


p = "(()())()"

def check(u):
    stack = []
    for i in u :
        if not stack:
            stack.append(i) 
        elif i == ')' :
            if stack[-1]  == '(':
                stack.pop()
            else :
                stack.append(i)
        else :
            stack.append(i)
    if stack :
        return False
    else :
        return True   

def solution(p):
    answer = ''
    count1 =0 
    count2 = 0 
    if p == '' :
        return answer
    u =''
    if check(p):
        return p
    else:
        for w in p :
            u += w
            if w == '(' :
                count1 +=1
            else :
                count2 +=1
            if count1 == count2 :
                break
        v = p[count1+count2:]
        # print(u)
        # print(v)
        
        #3 
        if check(u):
            answer = u + solution(v)
        else :
            answer = '(' + solution(v) + ')' 
            u = u[1:-1]
            reverse = ''
            for w in u :
                if w == '(':
                    reverse += ')'
                else :
                    reverse += '('
            answer = answer + reverse
            
        return answer

s = solution(p)
print(s)