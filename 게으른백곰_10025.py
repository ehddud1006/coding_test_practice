# import sys
# from collections import deque

# # 입력 
# input = sys.stdin.readline
# n,k = map(int,input().split())

# list = []
# for i in range(n) :
#     g,x = map(int,input().split())
#     list.append((g,x)) # 입력값을 list 에 저장하였습니다.

# # list를 sort 합니다. 튜플의 두번째 원소 기준입니다. 
# # ex 첫번째 원소 기준이라면 x[0] 로 하여야됩니다.
# # 그리고 오름차순이며, 내림차순으로 원할시 -x[1]으로 하여야합니다.
# list.sort(key=lambda x: x[1])
# max = list[-1][1]
# min = list[0][1]

# # 처음에는 덱으로 선언하지않고 리스트로 선언하였었는데요.
# # 이점에서 시간초과가 났습니다.
# # 일반적인 리스트(list)가 이러한 연산에 O(n)이 소요되는 데 반해, 덱(deque)은 O(1)로 접근 가능하기
# # 때문에 다시한번 시간복잡도에 대해 알 수 있는 계기가 되었습니다.
# sum1 = deque()
# line = [0] * (max+1) 

# answer = 0

# #리스트의 index를 x좌표 value를 g 값으로 생각하는게 
# # 편할 것 같아서 바꾸어 주었습니다.
# for value , x in list:
#     line[x]=value
# # print(line)

# # 그림 1 참고
# if max-min+1<2*k+1 :
#     answer = sum(line)
     
# else :  
          
#     for i in range(min, max+1-2*k) :
#         # 그림 2 참고 
#         if i == min :
#             for j in range(i, i+2*k+1) :
#                 sum1.append(line[j]) 
#             hap = sum(sum1) 
#             if answer < hap :
#                 answer =hap
#         # 그림 3 참고 
#         else :
#             a = sum1.popleft()
#             hap -= a
#             sum1.append(line[i+2*k])     
#             hap += line[i+2*k]  
#             if answer < hap :
#                 answer =hap 
 
# print(answer)
        
        
# import sys
# from collections import defaultdict
# input = sys.stdin.readline

# left, right : 양동이가 위치한 가장 좌측과 우측
# start, end : 투 포인터
# curr : 현재 얼음의 양

# n, k = map(int,input().rsplit())
# ice = defaultdict(int)
# min_l, max_l, answer = sys.maxsize, 0, -1

# for _ in range(n):
#     g, x = map(int,input().rsplit())
#     ice[x] = g
#     max_l = max(max_l, x)
#     min_l = min(min_l, x)

# end, curr = min_l, 0
# for start in range(min_l, max_l + 1):
#     while end < max_l + 1 and end - start <= k * 2:
#         if ice[end] == 0:
#             end += 1
#             continue
#         curr += ice[end]
#         end += 1
#     answer = max(answer, curr)
#     curr -= ice[start]
    

# print(answer)        