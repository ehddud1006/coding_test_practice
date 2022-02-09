import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

global ans
ans = 3000


def dfs(limit,total):
    # 꽃을 3개 심은경우 cost를 비교해서 더 적은 값이라면 ans에 넣는다.
    if limit == 3 :
        global ans 
        # print(total)
        ans = min(ans,total)
        return 
    # visit[x][y] = True
    
    for i in range(1,N-1):
        for j in range(1,N-1):
            # key 꽃을 심을 수 있는가 없는가 판단여부 
            key = False
            money = 0
            if not visit[i][j] :
                money += graph[i][j]
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    if visit[xx][yy] or xx < 0 or yy<0 or xx>=N or yy >= N :
                        break
                    if k == 3 :
                        key = True
                    money += graph[xx][yy]
            # 다 심을 수 있는경우 
            if key :
                # 다섯개의 칸 모두 visit 처리
                visit[i][j]=True
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    visit[xx][yy]=True
                # print(f'좌표: {i}, {j}')
                # print(f'money: {total+money}')
                dfs(limit+1,total+money)
                # dfs에서 나왔을때 visit을 다시 False로 변경
                for k in range(4):
                    xx = i + dx[k]
                    yy = j + dy[k]
                    visit[xx][yy]=False
                visit[i][j]=False

dfs(0,0)
print(ans)
        
    
        
    



        