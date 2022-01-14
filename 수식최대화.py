priority = [
    ["*","-","+"],
    ["*","+","-"],
    ["-","*","+"],
    ["-","+","*"],
    ["+","-","*"],
    ["+","*","-"],
]

expression = "100-200*300-500+20"

def solution(expression):
    
    
    for i in range(6):
        for j in range(3):
            index = 0  
            left=""
            right =""
            k=0
            p=0 
            if priority[i][j] == "*":
                for w in expression :
                    if w == "*" :
                        for k in range(index-1,-1,-1) :
                            if expression[k] == "-" or expression[k] == "+"  or expression[k] == "*":
                                left = expression[k+1:index]
                                break
                            elif k==0 :
                                left = expression[:index]
                                k=-1
                                break
                        for p in range(index+1,len(expression)) :
                            if expression[p] == "-" or expression[p] == "+"  or expression[p] == "*":      
                                right = expression[index+1:p]
                                break
                            elif p==len(expression) :
                                right = expression[index+1:p]
                                break
                        change = expression[k+1:p]              
                        l = int(left) 
                        r= int(right)            
                        go = abs(l * r)
                        expression = expression.replace(change,str(go))
                        print(expression)     
                    index +=1      
                      
                
                
            elif priority[i][j] == "-":
                for w in expression :
                    if w == "-" :
                        for k in range(index-1,-1,-1) :
                            if expression[k] == "-" or expression[k] == "+"  or expression[k] == "*":
                                left = expression[k+1:index]
                                break
                            elif k==0 :
                                left = expression[:index]
                                k=-1
                                break
                        for p in range(index+1,len(expression)) :
                            if expression[p] == "-" or expression[p] == "+"  or expression[p] == "*":      
                                right = expression[index+1:p]
                                break
                            elif p==len(expression) :
                                right = expression[index+1:p]
                                break
                        change = expression[k+1:p]              
                        l = int(left) 
                        r= int(right)            
                        go = abs(l - r)
                        expression = expression.replace(change,str(go))
                        print(expression)     
                    index +=1      
                      
                
                
            elif priority[i][j] == "+":
                for w in expression :
                    if w == "+" :
                        for k in range(index-1,-1,-1) :
                            if expression[k] == "-" or expression[k] == "+"  or expression[k] == "*":
                                left = expression[k+1:index]
                                break
                            elif k==0 :
                                left = expression[:index]
                                k=-1
                                break
                        for p in range(index+1,len(expression)) :
                            if expression[p] == "-" or expression[p] == "+"  or expression[p] == "*":      
                                right = expression[index+1:p]
                                break
                            elif p==len(expression) :
                                right = expression[index+1:p]
                                break
                        change = expression[k+1:p]              
                        l = int(left) 
                        r= int(right)            
                        go = abs(l + r)
                        expression = expression.replace(change,str(go))
                        print(expression)
                             
                    index +=1      
                      
                                     
                        
    answer = 0
    return answer

solution(expression)
