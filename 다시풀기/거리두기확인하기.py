from collections import deque
places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(x,y,seat) :
    visit = [[False]*5 for _ in range(5)]
    q = deque()
    visit[x][y]=True
    q.append((x,y,0))
    
    while q :
        
        x ,y, d = q.popleft()
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            
            if xx<0 or yy<0 or xx>=5 or yy>=5 or visit[xx][yy]==True:
                continue
            if seat[xx][yy] == 'O':
                q.append((xx,yy,d+1))
                visit[x][y]=True
            if  seat[xx][yy] == 'P' :
                d = d+1
                if d<=2 :
                    return False
            if seat[xx][yy] == 'X':        
                visit[x][y]=True
    return True
    
    
def solution(places):
    answer = []
    for i in range(len(places)):
        seat = []
        for data in places[i] :
            arr =[]
            for w in data :
                arr.append(w)
            seat.append(arr)
        test = set()
        for i in range(5):
            for j in range(5):
                if seat[i][j] == 'P':
                    if bfs(i,j,seat) :
                        test.add(1)
                    else :
                        test.add(0)
       
        if 0 in test :
            answer.append(0)
        else :
            answer.append(1)
    print(answer)
    return answer

solution(places)