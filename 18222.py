import math

# 깨닳은 점. math 메소드를 사용하면 float형이된다.
# 코테에서 float를 다루는 경우는 드물다. 고로 int로 형변환을 해주자.
# 이문제 같은 경우에도 다 맞춰놓고 pow의 float 형으로 인한 계산 오차때문에
# 맞추지 못하고 포기했다. 유성님이 피드백을 해주셔서 해답을 찾았다.
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