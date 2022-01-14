import copy 
# rows = 6
# columns = 6

# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

def rotate(board, queries,index,rows,columns):
    point1 = board[queries[index][0]-1][queries[index][3]-1]
    point2 = board[queries[index][2]-1][queries[index][3]-1]
    point3 = board[queries[index][2]-1][queries[index][1]-1]
    temp = board[queries[index][0]-1][queries[index][1]-1]
    # list_b = [item[:] for item in list_a]
    board_2 = [item[:] for item in board]
    for i in range(queries[index][1],queries[index][3]) :      
        a = board[queries[index][0]-1][i] 
        board[queries[index][0]-1][i] = temp 
        temp = a


    temp = point1
    for i in range(queries[index][0],queries[index][2]) :
        a =  board[i][queries[index][3]-1] 
        board[i][queries[index][3]-1] = temp 
        temp = a
    
    temp = point2
    for i in range(queries[index][3]-2,queries[index][1]-2,-1) :
        a =  board[queries[index][2]-1][i] 
        board[queries[index][2]-1][i] = temp 
        temp = a    
    
    temp = point3
    for i in range(queries[index][2]-2,queries[index][0]-2,-1) :
        a =  board[i][queries[index][1]-1] 
        board[i][queries[index][1]-1] = temp 
        temp = a    
    
    # for i in range(len(board)):
    #     print(board[i])
    mm= []
    for i in range(rows) :
        for j in range(columns) :
            if board_2[i][j] != board[i][j] :
                mm.append(board[i][j])
    return min(mm)




def solution(rows, columns, queries):
    answer = []
    
    board = [[0] * columns for _ in range(rows) ] 
    index = 1
    for i in range(rows) :
        for j in range(columns) :
            board[i][j] = index
            index+=1
    
    # for i in range(len(board)):
    #     print(board[i])
    
    for i in range(len(queries)):
        ans = rotate(board,queries,i,rows,columns)
        answer.append(ans)
    # print(answer)    
    return answer

a = solution(rows, columns, queries)
