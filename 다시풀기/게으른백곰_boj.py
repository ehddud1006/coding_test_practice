import sys
MIN = -sys.maxsize
# >>> import math

# >>> positive = math.inf              # 양의 무한대
# >>> print(positive)
# inf

# >>> negative = -math.inf             # 음의 무한대
# >>> print(negative)
# -inf
N,K = map(int,input().split())

location = []
weight = []

for i in range(N):
    a,b = map(int,input().split())
    location.append(b)
    weight.append(a)

maxi = max(location)
data = [0]*(maxi+1)
dp = [0]*(maxi+1)
dp[0]=data[0]
for i in range(len(location)):
    data[location[i]]=weight[i]

for i in range(1,len(data)):
    dp[i]=data[i]+dp[i-1]

start = 0
end = 0    
ans = MIN
while end <= maxi :
    step = dp[end]-dp[start]+data[start]
    
    if (end-start)<=2*K :
        end +=1
    else :
        start+=1
        continue
    
    if step > ans :
        ans = step
    
    
# print(data)
# print(dp)

print(ans)

