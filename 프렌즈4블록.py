m=6
n=6
board = 	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


dx = [0,1,1]
dy = [1,0,1]
map = []
visit = []
def bfs(i,j,target,map,visit) :
    count = 0
    for k in range(3):
        x = i + dx[k]
        y = j + dy[k]
        if x >= m or y >= n :
            continue
        if map[x][y] == target :
            count +=1
    bomb = 0        
    if count == 3 :
        visit[i][j] = True
       
        for k in range(3):
            x = i + dx[k]
            y = j + dy[k]
            if not visit[x][y] :
                bomb += 1
                visit[x][y] = True
                
        return bomb+1
    else :
        return bomb

def drop(i,j,target):
    original_i = i
    while True :
        i +=1 
        if map[i][j] != 'X':
            break
    map[original_i][j]='X'
    visit[original_i][j] = True
    map[i-1][j]=target
    visit[i-1][j] = False
    
        

def solution(m, n, board):
    answer = 0
    map = []
    visit = [[False]*n for _ in range(m)]
    for i in range(len(board)):
        map.append(list(board[i]))
        
    print(map)
    prev_answer = 0
    while True :
        for i in range(m):
            for j in range(n):
                target = map[i][j] 
                answer += bfs(i,j,target,map,visit) 
        
        for i in range(m):
            for j in range(n):
                if visit[i][j] :
                    map[i][j]="X"
        if prev_answer == answer :
            break
        else :
            prev_answer = answer 
        
        for i in range(m-2,0,-1):
            for j in range(n-1,0,-1):
                if map[i][j] != 'X':
                    drop(i,j,map[i][j])
        # if True :
        #     print("")
    print(answer)
    return answer

solution(m,n,board)