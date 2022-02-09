# people = [20,30,50,50,10,10,10]
# limit = 50
# dic = {}
# dic2 = {}
# def find(L):
#     for key,value in dic2.items() :
#         if key in dic and key<= L and value>0:
#             dic[key]-=1
#             dic2[key]-=1
#             break
    

# def solution(people, limit):
#     answer = 0
#     people.sort(reverse=True)
    
#     for i in range(len(people)):
#         if people[i] in dic :
#             dic[people[i]]+=1
#         else :
#             dic[people[i]]=1
    
#     people.sort()
    
#     for i in range(len(people)):
#         if people[i] in dic2 :
#             dic2[people[i]]+=1
#         else :
#             dic2[people[i]]=1
#     count = 0
#     step = 0
#     while len(dic)!=step:
#         step=0
#         # count += 1
#         for key, value in dic.items():
#             if value >0 :
#                 count += 1
#                 L = limit
#                 L-=key 
#                 dic[key]-=1
#                 dic2[key]-=1
#                 find(L)
#             else : 
#                 step +=1
#     # print(dic)
#     print(count)
#     return count

# solution(people,limit)

def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    while len(people) :
        
        
    return answer