p = "()))((()"
def check(u) :
    stack = []
    for w in u :
        if stack and stack[-1]=='(' :
            if w == ')' :
                stack.pop()
            else :
                stack.append(w)
        else :
            stack.append(w)
    if stack :
        return False
    else :
        return True
                    
def solution(p):
    # 1단계
    answer = ''
    
    if p == "" :
        return p
    
    # 2단계
    lc = 0
    rc = 0
    for w in p :
        if w == '(' :
            lc += 1
        elif w == ')' :
            rc += 1 
        
        if lc == rc :
            break
    u = p[:lc+rc]
    v = p[lc+rc:]       
    print(f'u :{u} v: {v}')
    
    ch= check(u) 
    
    # 3-1 단계
    if ch :
        return u + solution(v)
    else :
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        cute = ''
        for w in u :
            if w == '(' :
                cute += ')'
            elif w == ')' :
                cute += '('
        return answer + cute       


a = solution(p)
print(a)