import sys
input = sys.stdin.readline
N = int(input())

data = list(map(int,input().split()))
data.sort()

mmin = (3e9+1)
answer = ()
# 중복되는 pointer가 없도록 하기위해서 N-2이다.
for lp in range(N-2):
    
    mp , rp = lp + 1, N-1 
    while mp < rp :
        sum = data[lp] + data[mp] + data[rp]
        abs_sum = abs(sum) 
        if abs_sum < mmin :
            mmin = abs_sum
            answer = (data[lp],data[mp],data[rp])
            if mmin == 0 :
                break
        if sum > 0 :
            rp -=1
        else :
            mp +=1
# print(answer)
print(*answer)