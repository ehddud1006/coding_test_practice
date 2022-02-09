import sys

#입출력
input = sys.stdin.readline
N = int(input())
data = list(map(int,input().split()))

#오름차순 정렬
data.sort()
# print(data)

start = 0
end = len(data)-1

# 최대로 나올수 있는 값이 2000000000
# 문제에서  1부터 1,000,000,000까지의 양의 정수 라고 명기
ab = 2000000000
# 0으로 초기화 한 이유는 없습니다. 아무 숫자를 넣어 초기화하였다.
a = 0
b = 0

# 여기서 왜 ? start < end 인가?
# 기존의 투 포인터는 start <= end 이지 않는가?
# 7
# # -2 4 -99 -1 0 98 11
# 위의 예시를 보면, start <= end의 경우 
# start 와 end가 모두 0인 경우가 발생할 수 있다.
# 용액은 하나인데 두번 사용하는 경우이다.
# 이러한 케이스를 제외하기 위해 start<end를 조건으로 선언하였습니다.
while start < end :
    # target , ab_target을 각각 선언한 이유는,
    # target은 절댓값을 취하지 않고 target이 0보다 작다면
    # start + 1 을 하게 되면 즉, 현재 start보다 더 큰 값을 더하게 된다면
    # 0에 가까운 수가 될 수 있기때문에.
    # 예를 들면 
    # [-99, -98, -1, 0, 4, 11, 98]
    # start                   end  현재값 -1
    #       start             end  현재값 0 
    # 위와 같은 결과를 얻을 수 있습니다.
    
    # 반대로, target이 0 보다 크다면, end-1 을 하여 
    # 0에 가까운 수가 될 수 있도록 합니다.
    
    # 그리고 그 과정에서 절댓값이 작은 수일때 start와 end를
    # 저장하기위하여 ab_target을 사용합니다.
    target =data[start]+data[end]
    ab_target = abs(target)
    if target == 0 :
        a = start
        b = end 
        break
    elif target < 0 :
        if ab > ab_target :
            ab = ab_target 
            a = start
            b = end 
        start+=1
    else :
        if ab > ab_target :
            ab = ab_target 
            a = start
            b = end
        end-=1

print(f'{data[a]} {data[b]}')
