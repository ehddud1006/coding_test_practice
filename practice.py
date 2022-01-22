import sys

N = int(input())
want = list(map(int,input().split()))
budget = int(input())

all_sum = sum(want)
max_want = max(want)
mid = 0
if all_sum <= budget :
    print(max_want)
else :
    start = 0
    end = max_want
    mid = (start+end)//2
    while start <= end :
        
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
        mid = (start+end)//2
print(mid)
                