# from itertools import permutations

n=12
weak =[1, 5, 6, 8, 10]
dist = [1, 2, 3, 4]

from itertools import permutations
def solution(n, weak, dist):
    original_weak_length = len(weak)
    answer = 0
    # 왜 원형의 * 2 를 하면 방향을 고려하지 않아도 될까?
    # 그 이유는 , [1,5,6,10] 에서 3 지점을 정해야한다고 할때,
    # 1,5,6 / 5,6,10 / 6,10,13(n=12이므로) 와 같이 한바퀴
    # 돌아서? 정할 수 있게됩니다.  
    for i in range(len(weak)):
        weak.append(weak[i]+n)
    
    # 어떤 친구가 먼저 검사할지 정합니다.
    who_visit_weak = list(permutations(dist,len(dist))) 
    
    # 벽을 어떤순서로 점검할 것인지 정합니다.
    # [1,5,6,8,10,13,17,18,20,22]
    # 시작점을 달리하여 점검하기 위함입니다.
    visit_weak_orders = []
    for i in range(original_weak_length):
        temp = []
        for j in range(i,original_weak_length+i) :
            temp.append(weak[j])
        visit_weak_orders.append(temp)
    
    # 친구수 (dist) 8이하 이기때문입니다.
    answer = 9
    
    # [1,5,6,8,10]
    # [1,2,3,4]
    for visit_weak_order in visit_weak_orders :
        for who in who_visit_weak :
            key = True
            count = 1
            # who 의 인덱스를 다루기위함
            friend_index = 0
            # visit_weak_order를 다루기 위함.
            wall_index = 0
            
            #첫번째 주자가 점검할 수 있는 범위를 limit으로 정합니다.
            # 1을 시작으로해서 첫번째 주자가 점검할 수 있는 범위의 값을 정한다.
            # limit = 2
            limit = visit_weak_order[wall_index]+who[friend_index]
            
            # 모든 벽을 점검했다면 while문을 탈출합니다.
            #         0               5
            while wall_index<len(visit_weak_order) :
                # 벽의 위치가 해당 주자가 점검할 수 있는 위치 밖일 경우입니다.
                if visit_weak_order[wall_index] > limit :
                    # 모든 주자가 탐색을 완료한 경우에
                    if friend_index == len(who)-1:
                        key = False
                        break
                    # 다음주자로 넘겨줍니다.
                    count +=1
                    friend_index += 1
                    
                    # 다음주자가 점검할 수 있는 범위로 limit을 갱신합니다.
                    limit = visit_weak_order[wall_index]+who[friend_index]
                    
                else :
                    # 다음 점검할 벽의 index입니다.
                    wall_index += 1
                    
            # 제 로직에서는 break 를 통해서 while이 빠져나온 경우에는 answer를 갱신해주어선 안됩니다.
            if key :
                answer = min(answer,count)
    # print(answer)
    
    # answer 가 9라면, 총 친구수가 8명이기 때문에 점검 할 수 없는 벽이므로 -1을 return
    if answer == 9 :
        return -1
    else :
        return answer

solution(n,weak,dist)