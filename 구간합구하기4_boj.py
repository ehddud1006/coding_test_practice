import sys
input = sys.stdin.readline

# ans = dp[b-1]-dp[a-1]+data[a-1]

N, M = map(int,input().split())

data = list(map(int,input().split()))
dp = [0]*(N)
dp[0]=data[0]
for i in range(1,N):
    dp[i]=data[i]+dp[i-1]
    
for i in range(M):
    a , b = map(int,input().split())
    ans = dp[b-1]-dp[a-1]+data[a-1]
    print(ans)
    