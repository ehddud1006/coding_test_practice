from itertools import combinations
orders =["XYZ", "XWY", "WXA"]
course = [2,3,4]
dict = {}
answer= []
new_orders = []

for word in orders :
    go = []
    for w in word :
        go.append(w)
    go.sort()
    gg = ''
    for w in go :
        gg += w
    new_orders.append(gg)
# print(new_orders)                
for order in new_orders :
    for i in range(len(course)):
        if len(order) >= course[i]:
            list1 = list(combinations(order,course[i]))
            for j in list1 :
                ans = ''
                for k in range(course[i]) :
                    ans += j[k]
                if ans not in dict :    
                    dict[ans]=1    
                else :
                    dict[ans]+=1    
           

for i in range(len(course)):
    max = 0
    for key , value in dict.items():   
        if value >= max and len(key) == course[i] :
            max = value  
    if max >= 2:          
        for key , value in dict.items():   
            if value == max  and len(key) == course[i]  :
                answer.append(key)                                        
# print(dict)
  
answer.sort()
print(answer) 
