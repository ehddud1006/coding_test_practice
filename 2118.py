import sys 
input = sys.stdin.readline

# https://www.acmicpc.net/problem/2118
# https://doooooooong.tistory.com/51
# https://9327144.tistory.com/entry/BOJ-2118-%EB%91%90-%EA%B0%9C%EC%9D%98-%ED%83%91JAVA
# 너무 어려운 투포인터 다시보고 문제 풀면서 이해해나가자.
N = int(input())
dist = []
dist.append(0)
dp = [0]*(N+1)
for i in range(N):
    dist.append(int(input()))

for i in range(1,N+1):
    dp[i]=dp[i-1]+dist[i]

# print(dp)

start = 0
end = 1
ans = -100000000
while end<= N :
    clockwise = dp[end]-dp[start]
    unclockwise = dp[N]-clockwise
    mini = min(unclockwise,clockwise)
    if ans < mini:
        ans = mini
    if clockwise<unclockwise :
        end +=1
    else :
        start +=1

print(ans)