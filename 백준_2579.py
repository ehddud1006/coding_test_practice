n = int(input())

point = [0] * (n+1)
dp = [0] * (n+1)
# 첫번째 계단 = 1 로 두기위해서 n+1을 사용 (0이 아닌)

for i in range(1,n+1):
    point[i] = int(input())
# 계단 점수를 point 배열에 넣는다.

# 혹시나 n이 1이나 2 같은 수가 들어오면 오류가 생길까봐 if문을 사용했습니다.        
if n >= 1 :    
    dp[1]=point[1]
    
if n>=2 :
    dp[2]=point[1]+point[2]

if n>=3 :
    dp[3]=max(point[1]+point[3],point[2]+point[3])
    #첫번째계단 + 세번째 계단, 두번째계단 + 세번째 계단중 큰 값을 선택합니다.

if n>=4 :
    for i in range(4,n+1):
        dp[i] = max(dp[i-2]+point[i],dp[i-3]+point[i-1]+point[i])
        # 예를들어 n=4 일 경우
        # 2번쨰 계단누적합 + 4번째 계단 , 1번째게단 누적합 + 3번째 4번째계단중 
        # 큰값을 선택합니다.

print(dp[n])