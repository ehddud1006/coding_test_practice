participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

dict = {}
answer = ''

for i in participant :
    if i in dict :
        dict[i]+=1
    else:
        dict[i]=1

for i in completion :
    if i in dict :
        dict[i]-= 1
    
for key , value in dict.items() :
    if value > 0 :
        answer = key
        break
   
    # print(f'key: {key} value: {value}')        
print(dict)        