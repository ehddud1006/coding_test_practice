

number = "1111111"
k = 2

def solution(number, k):
    answer = ''
    stack = []
    for w in number :
        if len(stack) == 0 :
            stack.append(w)
        else :
            if k == 0 :
                stack.append(w)
            elif stack[-1]< w :
                stack.pop()
                k-=1
                while len(stack)>0 and stack[-1]< w and k>0 :
                    stack.pop()
                    k-=1
                stack.append(w)    
            else :
                stack.append(w)
    
    # print(stack)
    for w in stack :
        answer += w

    # 111111 K가 줄어들지 않는 경우
    if len(answer)>len(number)-k:
        f = len(answer) - (len(number)-k) 
        answer = answer[:-f]
    print(answer)
    
    
solution(number,k)