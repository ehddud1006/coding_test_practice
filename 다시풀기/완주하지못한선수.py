participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]	

dict = {}

for i in participant :
    if i in dict :
        dict[i]+=1
    else:
        dict[i]=1

for i in completion :
    if i in dict :
        dict[i]-=1

print(dict)

for key,value in dict.items():
    if value > 0 :
        answer = key