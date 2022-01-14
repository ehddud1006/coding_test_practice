import sys

input = sys.stdin.readline

n = int(input())

love = [[0]*5 for _ in range(n*n) ]
classroom = [[0]*(n) for _ in range(n) ]
student_location = {}
sum = 0
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

manjok_x = [-1,1,0,0]
manjok_y = [0,0,-1,1]
for i in range(n*n) :
    love[i] = list(map(int,input().split()))

information = [[0]*(n) for _ in range(n) ]
empty_seat_information = [[0]*(n) for _ in range(n) ]
#1
for i in range(len(love)) :
    student = love[i][0]
    information = [[-1]*(n) for _ in range(n) ]
    for p in range(len(classroom)):
        for j in range(len(classroom)):
            seat = classroom[p][j]
            count = 0   
            if seat == 0 :     
                for k in range(1,5):
                    love_student = love[i][k]
                    if love_student in student_location :
                        x,y = student_location[love_student]
                        dist = abs(p-x)+abs(j-y)  
                        if dist == 1 :
                            count +=1
                information[p][j] = count            
    
    go_x = 0
    go_y = 0
    best_location = -1
    for p in range(len(information)):
        for j in range(len(information)):
            if information[p][j]>best_location :
                best_location = information[p][j]
                go_x=p
                go_y=j
    # print(information)
                                    
    #2 
    count = 0
    for p in range(len(information)):
        for j in range(len(information)):
            if best_location == information[p][j] :
                count +=1

    if count == 1 :
        student_location[student] = (go_x,go_y)
        classroom[go_x][go_y]=student
                
    else :
        empty_seat_information = [[-1]*(n) for _ in range(n) ]
        remember_max = -1
        remember_x = 0
        remember_y = 0
        for p in range(len(empty_seat_information)):
            for j in range(len(empty_seat_information)):
                if best_location == information[p][j] :
                    emptycount = 0
                    for k in range(4) :
                        x = p + manjok_x[k]
                        y = j + manjok_y[k]
                        if x<0 or y<0 or x>=n or y>=n:
                            continue
                        if classroom[x][y]==0 :
                            emptycount+=1
                    empty_seat_information[p][j]=emptycount    
                    if emptycount>remember_max:
                        remember_max=emptycount
                        remember_x = p
                        remember_y = j
        student_location[student] = (remember_x,remember_y)
        classroom[remember_x][remember_y]=student
                             
        
# for i in range(len(classroom)):
#     print(classroom[i])                
                
                 


for i in range(len(love)):
    student = love[i][0]
    count = 0
    for j in range(len(classroom)):
        for k in range(len(classroom)):
            if classroom[j][k] == student :
                for p in range(4) :
                    x = j + manjok_x[p]
                    y = k + manjok_y[p]
                    if x<0 or y<0 or x>=n or y>=n:
                        continue
                    for o in range(1,5):
                        if love[i][o]==classroom[x][y] :
                            count+=1
    if count==0 :
        sum+=0
    elif count == 1 :
        sum+=1
    elif count == 2 :
        sum+=10  
    elif count == 3 :
        sum+=100  
    elif count == 4 :
        sum+=1000                    
                 
print(sum) 
# print(love) 