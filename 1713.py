import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
chuchun = [1001]*(101)
dic = {}

guide = list(map(int,input().split()))

for i in range(len(guide)):
    step = guide[i]
    
    if len(dic) == N and step not in dic:
        minimum  = min(chuchun)
   
        for key, value in dic.items() :
            if value == minimum :
                dic.pop(key)
                chuchun[key] = 1001
                dic[step]=1
                chuchun[step]=1
                break
                            
    else :
        if step in dic :
            dic[step] += 1
            chuchun[step] += 1
           
        else :
            dic[step]=1
            chuchun[step] = 1
           

dic = sorted(dic.items(), key=lambda x: x[0])
for i in range(len(dic)):
    print(f'{dic[i][0]}',end=" ")
   
        
        
    