graph = [list(map(int,input().split())) for _ in range(9)]
go = set([0,1,2,3,4,5,6,7,8,9])

def rowrow():
    for i in range(9):
        zero_count = 0
        zero_index = 0
        go = set([0,1,2,3,4,5,6,7,8,9])
        for j in range(9):
            if graph[i][j]==0:
                zero_count+=1
                zero_index = j
        if zero_count == 1:
            go -= set(graph[i])
            gogo = list(go)
            print(gogo[0])
            graph[i][zero_index]=gogo[0]

def colcol() :
    for i in range(9):
        zero_count = 0
        zero_index = 0
        go = set([0,1,2,3,4,5,6,7,8,9])
        data = set()
        for j in range(9):
            if graph[j][i]==0:
                zero_count+=1
                zero_index = j
            data.add(graph[j][i])
        if zero_count == 1:
            go -= set(data)
            gogo = list(go)
            print(gogo[0])
            graph[zero_index][i]=gogo[0]

def dfs(x,y) :
    if x>6 or y>6 :
        return
    zero_count = 0
    zero_i = 0
    zero_j = 0
    go = set([0,1,2,3,4,5,6,7,8,9])
    data = set()
    for i in range(x,x+3):
        for j in range(y,y+3):
            if graph[i][j]==0:
                zero_count+=1
                zero_j = j
                zero_i = i
            data.add(graph[i][j])
    if zero_count == 1:
        go -= set(data)
        gogo = list(go)
        print(gogo[0])
        graph[zero_i][zero_j]=gogo[0] 
    dfs(x+3,y)
    dfs(x,y+3)

while True :
    count = 0
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0 :
                count +=1
    if count == 0 :
        break
    else :
        rowrow()
        colcol()
        dfs(0,0)
        
for i in range(9):
    print(*graph[i])