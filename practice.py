board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]

from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

dxx = [0,1,0,-1]
dyy = [1,0,-1,0]

def solution(board):
    answer = 0
    n = len(board)
    def bfs(xxx,yyy,ccc,dr) :
        q = deque()
        visit = [[0]*n for _ in range(n)]
        q.append((xxx,yyy,ccc,dr))
        visit[xxx][yyy] = 100
        index = 0
        while len(q)!= 0 and index != 10:
            x,y,c,r = q.popleft()
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
            
                direction = i
                if xx<0 or yy<0 or xx >= n or yy >=n :
                    continue
                if board[xx][yy] == 1 : 
                    continue
                
                cc = c
                if direction == r :
                    cc = c + 100
                else :
                    if r == 0 and direction != 2 :
                        cc = c + 600 
                    elif r == 1 and direction != 3 :
                        cc = c + 600
                    elif r == 2 and direction != 0 :
                        cc = c + 600
                    elif r == 3 and direction != 1 :
                        cc = c + 600
                #print(f'xx:{xx}, yy:{yy}, cc:{cc}, d:{direction}')
                if visit[xx][yy] < cc and visit[xx][yy]!=0:
                    continue
                q.append((xx,yy,cc,direction))
                print(q)
                visit[xx][yy]=cc
                for i in range(n):
                    print(visit[i])
                index +=1
                print(index)
        for i in range(n):
            print(visit[i])
        print(visit[n-1][n-1])
        return visit[n-1][n-1]
    case1 = bfs(0,0,0,1)
    case2 = bfs(0,0,0,2)
    answer = min(case1,case2)
    print(answer)                
    return answer

solution(board)