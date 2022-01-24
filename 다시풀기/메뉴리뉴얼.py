
from itertools import combinations
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
#  orders_list = list(orders[i])
#         print(orders_list)
#         print(*orders_list)
# ['A', 'B', 'C', 'F', 'G']
# A B C F G
# ['A', 'C']
# A C
# ['C', 'D', 'E']
# C D E
# ['A', 'C', 'D', 'E']
# A C D E
# ['B', 'C', 'F', 'G']
# B C F G
# ['A', 'C', 'D', 'E', 'H']
# A C D E H
ssize = [0]*11
def solution(orders, course):
    answer = [] 
    dic = {}
    for i in range(len(orders)):
        orders_list = list(orders[i])
        orders_list.sort()
        for j in range(len(course)):
            go = list(combinations(orders_list,course[j]))
            for order in go :
                menu = ''
                for k in order :
                    menu+=k
                if menu in dic :
                    dic[menu]+=1
                else :
                    dic[menu]=1
    print(dic)
    for i in range(len(course)):
        target = course[i]
        max = 0
        for a,b in dic.items() :
            if len(a) == target :
                if max < b :
                    max = b
        ssize[course[i]]=max            
                
    print(ssize)
    # print(answer)
            
    for a,b in dic.items() :
        if b == ssize[len(a)] :
            answer.append(a)
    answer.sort()
    print(answer)
    return answer

solution(orders,course)

