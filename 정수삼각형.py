triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    n,m = len(triangle) , len(triangle[-1])
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1]=triangle[0][0] 
    for i in range(1,n):
        for j in range(i+1):
            dp[i+1][j+1] = triangle[i][j] + max(dp[i][j+1],dp[i][j])  
    
    answer = max(dp[-1])
    # print(answer)
    return answer

solution(triangle)