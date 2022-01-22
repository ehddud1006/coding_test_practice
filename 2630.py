
import sys 

N = int(input()) 
graph = [[]*N for _ in range(N)]

for i in range(N):
    graph[i]=list(map(int,input().split())) 

# print()
# for i in range(N):
#     print(graph[i])
global blue 
global white 
blue = 0
white = 0
def sol(a,b,size):
    global blue
    global white 
    if size == 0 :
        return
    count1 = 0
    count2 = 0
    for i in range(a,a+size):
        for j in range(b,b+size):
            if graph[i][j] == 1 :
                count1 +=1
            else :
                count2 +=1 
                
    if count1 == size * size :
        blue +=1
        return
    elif count2 == size * size :
        white +=1 
        return
    sol(a,b,size//2)
    sol(a,b+size//2,size//2)
    sol(a+size//2,b,size//2)
    sol(a+size//2,b+size//2,size//2)

sol(0,0,N)
print(white)
print(blue) 
        
    