def conversion_logs(log, dp) :
    data = list(log.split('-'))
    #print(data)
    start = conversion_of_playtime_to_advertising_time_seconds(data[0])
    end = conversion_of_playtime_to_advertising_time_seconds(data[0])
    dp[start] += 1 
    dp[end] -= 1

def conversion_of_playtime_to_advertising_time_seconds(target) :
    target_split_data = list(target.split(':'))
    #print(target_split_data)
    hour = int(target_split_data[0])
    minute = int(target_split_data[1])
    second = int(target_split_data[2])
    total_second = hour*3600 + minute*60 + second
    return total_second
def solution(play_time, adv_time, logs):
    answer = ''
    dp = [0]*360000
    play_time_to_second = conversion_of_playtime_to_advertising_time_seconds(play_time)
    #print(play_time_to_second)
    adv_time_to_second =conversion_of_playtime_to_advertising_time_seconds(adv_time)
    
    for log in logs :
        conversion_logs(log,dp)
    #print(dp)    
    
    for i in range(1,36000) :
        dp[i]=dp[i]+dp[i-1]
        
    for i in range(1,36000) :
        dp[i]=dp[i]+dp[i-1]
    
    mmax = 0
    index = 0
    for i in range(adv_time_to_second,360000) :
        tt = dp[i]-dp[i-adv_time_to_second]
        if tt > mmax :
            index = i
            mmax = tt
    
    h = index // 3600
    m = (index % 3600) // 60
    s = (index % 3600) % 60
    
    if len(str(h)) == 1 :
        hh = "0"+str(h)
    if len(str(m)) == 1 :
        mm = "0"+str(m)
    
    if len(str(s)) == 1 :
        ss = "0"+str(s)
    ans = hh+":"+mm+":"+ss
    return ans