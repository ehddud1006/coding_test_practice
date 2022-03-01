m=4
n=3
puddles=[[2, 2]]
def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+2) for _ in range(n+2)]
    puddle = [[True]*(m+2) for _ in range(n+2)]
    for pud in puddles :
        y,x = pud
        puddle[x][y]= False
    dp[1][1]=1
    for i in range(n):
        for j in range(m):
            if puddle[i+1][j+1] :
                dp[i+1][j+1] = dp[i+1][j+1] + dp[i][j+1] + dp[i+1][j]
    answer = dp[n][m]
    print(answer)
    return answer

solution(m,n,puddles)