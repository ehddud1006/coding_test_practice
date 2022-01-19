import sys 
input = sys.stdin.readline

N = int(input())
dist = []
dist.append(0)
dp = [0]*(2*N+1)
for i in range(N):
    dist.append(int(input()))

for i in range(1,N+1):
    dp[i]=dp[i-1]+dist[i]

for i in range(1,N+1):
    dp[i+N]=dp[i+N-1]+dist[i]

# print(dp)
mmax = 0
for i in range(1,N+1):
    for j in range(i+1,N+1) :
        a= dp[j-1]-dp[i-1]
        b=dp[j-2+N]-dp[i]
        m = min(dp[j-1]-dp[i-1],dp[i-1+N]-dp[j-1])
        
        if m > mmax :
            mmax = m

print(mmax)            