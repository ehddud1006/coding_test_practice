import sys 
from itertools import combinations
input = sys.stdin.readline

icecream = []
dic = {}

count = 0
n,m = map(int,input().split())

for i in range(1,n+1):
    icecream.append(i)
    
for i in range(1, n + 1):
    dic[i] = []
    
for i in range(m) :
    a,b = map(int,input().split())
    if a>b :
        dic[b].append(a)
    else :
        dic[a].append(b)
    

print(dic)

random_select_three = combinations(icecream,3)
random_select_three_list = list(random_select_three)    

for i in range(len(random_select_three_list)):
    a,b,c = random_select_three_list[i]
    if c in dic[a] or c in dic[b] or b in dic[a] :
        continue
    count +=1
    # print(a,b,c)

print(count)
    
