board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]

def solution(board, skill):
    answer = 0
    dp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    # print(dp)
    for s in skill :
        ttype , r1 , c1 , r2 , c2 ,degree = s
        if ttype == 1:
            dp[r1][c1]+=-degree
            dp[r1][c2+1]+=degree
            dp[r2+1][c1]+=degree
            dp[r2+1][c2+1]+=-degree
        if ttype == 2:
            dp[r1][c1]+=degree
            dp[r1][c2+1]+=-degree
            dp[r2+1][c1]+=-degree
            dp[r2+1][c2+1]+=degree
    
    # print(dp)
    for i in range(len(board)):
        for j in range(1,len(board[0])):
            dp[i][j]=dp[i][j-1]+dp[i][j]
            
    for i in range(len(board[0])):
        for j in range(1,len(board)):
            dp[j][i]=dp[j-1][i]+dp[j][i]

    # print(dp)
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += dp[i][j]
    
    # print(board)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]>0 :
                answer+=1 
    # print(answer)
    return answer

solution(board,skill)