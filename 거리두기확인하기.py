from collections import deque

places =[["POOOX", "XXXOX", "POOOX", "OXOOX", "POOOO"]]

def bfs(a,b,dist,wait_room):
    visited = [[False]*5 for _ in range(5)]
    queue = deque()
    queue.append((a,b,dist))
    visited[a][b] = True

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    while queue :
        
        n,m,d = queue.popleft()
        if d > 2 :
            continue
        
        for i in range(4):
            x = n+dx[i]
            y = m+dy[i]
            
            
            if x<0 or y<0 or x>=5 or y>=5 :
                continue
            if wait_room[x][y]=='X'  :
                visited[x][y]=True
                continue
            if wait_room[x][y]=='P' and not visited[x][y] and d<2:
                return 0
            if wait_room[x][y]=='O' and not visited[x][y] :
                visited[x][y]=True
                queue.append((x,y,d+1))
    return 1            
            
def creat_wait_room(i,places) :
    wait_room = [['']*5 for _ in range(5)]
    for j in range(5):
            ss = places[i][j]
            for k in range(5):
                wait_room[j][k]=ss[k]
    return wait_room
            
def solution(places):
    answer = []
    key = False
    
    for i in range(len(places)) :
        no_people = True
        wait_room = creat_wait_room(i,places)
        for f in range(5):
            print(wait_room[f])
        print()
        people_num = 0
        sum = 0
        for a in range(5) :
            for b in range(5):
                if wait_room[a][b]=='P' :
                    people_num+=1
                    no_people = False
                    sum += bfs(a,b,0,wait_room)
                    
        if people_num == sum :
            answer.append(1)                   
        else :
            answer.append(0)  
    return answer        

a = solution(places)
print(a)



