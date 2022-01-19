import sys
input = sys.stdin.readline
N = int(input())
want = list(map(int,input().split()))
budget = int(input())

all_sum = sum(want)
max_want = max(want)
mid = 0

#초기국가 예산으로 지방예산요청을 수용이 가능한 경우
if all_sum <= budget :
    print(max_want)
else :
    start = 0
    end = max_want
#이분 탐색
    while start <= end :
        mid = (start+end)//2
        all_budget = 0
        for i in range(N):                
            if mid > want[i]:
                all_budget += want[i]
            else:
                all_budget += mid
        
        if all_budget==budget :
            break
        
        elif all_budget>budget :
            end = mid-1
        
        else :
            start = mid+1
    
#이분탐색을 종료 했는데 
#4
#120 110 140 150
#485
# 의 출력값이 128이 나오고 (답은 127)
# 또
# 3
# 100 110 120
# 300
# 의 출력값은 99가 나왔었습니다. (답은 100)
# 그래서 mid값에 뭔가 문제가 있어서 
# mid값으로 예산계산을 해서 국가예산보다 더 큰경우에는 mid-1을 해주고,
# 그렇지 않은 경우에는 mid + 1 을 해주어 
# 또한번 예산을 진행합니다. 계산결과로 국가예산이 더 큰경우는 mid-1 
# 아니라면 mid를 그대로 사용합니다.
    all_budget = 0  
    for i in range(N):                
        if mid > want[i]:
            all_budget += want[i]
        else:
            all_budget += mid
     
    if all_budget>budget :
            mid = mid-1
    else :
        mid = mid+1
        all_budget = 0 
        for i in range(N):                
            if mid > want[i]:
                all_budget += want[i]
            else:
                all_budget += mid
                
        if all_budget>budget :
                mid = mid-1

    
    print(mid)