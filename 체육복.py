n=5
lost = [2, 4]
reserve = [1, 3, 5]	

dict = {}

for i in range(1,n+1) :
    dict[i] = 0 

for index , value in enumerate(lost):
    dict[value]-=1

for index , value in enumerate(reserve):
    dict[value]+=1

for index , value in enumerate(reserve):
    print(f'index: {index} value: {value}')
    if value-1 in dict :
        if dict[value-1] == -1 :      
            dict[value-1] = 0
            dict[value]=0
        elif value +1 in dict :
            if dict[value+1] == -1 :          
                dict[value+1] = 0
                dict[value]=0   
    elif value +1 in dict :
        if dict[value+1] == -1 :
            
            dict[value+1] = 0
            dict[value]=0         
    
print(dict)
count = 0
for key, value in dict.items():
    if value >= 0 :
        count +=1

print(count)