import sys

input = sys.stdin.readline

N , M = map(int,input().split())

dic = {}

for i in range(N) :
    strr = input().rstrip()
    if strr not in  dic :
        dic[strr]=1


for i in range(M) :
    strr = input().rstrip()
    if strr in dic :
        dic[strr]+=1

ans = 0
  
for key, value in dic.items() :
    if value > 1 :
        ans += value -1
# print(dic)
print(ans)