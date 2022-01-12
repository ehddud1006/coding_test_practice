s = "baabaa"

list = [] 

for i in s : 
    if len(list)>0 :
        if list[-1]== i :
            list.pop()
        else :
            list.append(i)
    else :
        list.append(i)    

if list :
    answer = 1
else :
    answer = 0       