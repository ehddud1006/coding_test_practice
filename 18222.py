# import math
# # N = int(input())
# global ans
# ans = -1
# arr1 = []
# arr2 = []
# def divide(depth,N):
#     global ans
#     expo = 1
#     if N==1 :
#         if depth % 2 == 0 :
#             ans=0
#             return
#         else :
#             ans=1
#             return
    
#     if N==2 :
#         if depth % 2 == 0 :
#             ans=1
#             return
#         else :
#             ans=0
#             return    
        
#     while True :
#         if math.pow(2,expo) < N and N <= math.pow(2,expo+1) :
#             N = N - math.pow(2,expo) 
#             divide(depth+1,N)
#             break
#         expo +=1 
        
#     return      

# # divide(0,N)
# # print(ans)
# for i in range(1,100000):
#     divide(0,i)
#     arr1.append(ans)


# import sys
# from math import log2

# input = sys.stdin.readline


# def solution(k: int) -> chr:
#     cnt_swap = 0
#     while k > 1:
#         biggest_power_of_2 = 2 ** int(log2(k-1))   # biggest_power_of_2: k보다 작은 2의 거듭제곱 중 최댓값
#         k -= biggest_power_of_2
#         cnt_swap += 1

#     if cnt_swap % 2 == 0:
#         char = '0'
#     else:
#         char = '1'
#     return char

# for i in range(1,100000):
 
#     sol = solution(i)
#     arr2.append(int(sol))

# for i in range(len(arr1)):
#     print(i)
#     if arr1[i] != arr2[i] :
       
#         print(f'i: {i}')


import math

N = int(input())
index = 0
while True :
    if N == 1 :
        if index % 2 == 0 :
            print(0)
        else :
            print(1)
        break
    
    if N == 2 :
        if index % 2 == 0 :
            print(1)
        else :
            print(0)
        break
    
    
    cha = 2 ** int(math.log2(N-1))
    N -= cha
    index += 1


