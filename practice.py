import math
N = int(input())

def divide(depth,N):
    expo = 1
    if N==1 :
        if depth % 2 == 0 :
            print(0)
            return
        else :
            print(1)
            return
    
    if N==2 :
        if depth % 2 == 0 :
            print(1)
            return
        else :
            print(0)
            return    
        
    while True :
        if int(math.pow(2,expo)) < N and N <= int(math.pow(2,expo+1)) :
            N = N - int(math.pow(2,expo)) 
            divide(depth+1,N)
            break
        expo +=1 
        
    return      


divide(0,N)