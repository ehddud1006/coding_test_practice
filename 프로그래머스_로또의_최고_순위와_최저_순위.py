lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
zero_count = 0
correct_count = 0

rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
answer = []
for i in range(6) :
    if lottos[i] == 0 :
        zero_count+=1
        
for  i in range(6) :
    for j in range(6):
        if win_nums[j] == lottos[i] :
            correct_count+=1
            break
            

answer.append(rank[correct_count+zero_count])
answer.append(rank[correct_count])


# def solution(lottos, win_nums):
    
#     rank=[6,6,5,4,3,2,1]

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans]