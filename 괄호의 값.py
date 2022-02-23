


strr = input()
#1
def check() :
    stack = []
    for w in strr :
        if len(stack)>0 and stack[-1] == "(" and w == ")" :
            stack.pop()
        elif len(stack)>0 and stack[-1] == "[" and  w == "]" :
            stack.pop()
        else :
            stack.append(w)

    if len(stack) == 0 :
        return True
    else :
        return False

#2
if check() :
    stack = []
    tmp = 0
    for w in strr :
        if w == ")" :
            tmp = 0
             #4
            while True :
                target = stack.pop()
                if target == "(":
                    break
                else :
                    tmp += target
            #4-2  
            if tmp == 0 :
                stack.append(2)
            #4-1 
            else :
                stack.append(2*(tmp))
        elif  w == "]" :
            tmp = 0
             #4
            while True :
                target = stack.pop()
                if target == "[":
                    break
                else :
                    tmp += target
            #4-2        
            if tmp == 0 :
                stack.append(3)
            #4-1                
            else :
                stack.append(3*(tmp))
        else :
            stack.append(w)
    #5-1
    if len(stack)> 0 :
        tmp = 0
        while len(stack):
            tmp += stack.pop()
        print(tmp)
    #5-2    
    else :
        print(tmp)
else :
    print("0")
    