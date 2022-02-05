from multiprocessing.sharedctypes import Value
import sys
input = sys.stdin.readline

dic = {}

while True:
    strr = input().rstrip()
    
    if strr == '' :
        break
    
    if strr in dic :
        dic[strr]+=1
    else :
        dic[strr]=1

total = 0
for key , value in dic.items() :
    total += value
    
print(total)    
print(dic)