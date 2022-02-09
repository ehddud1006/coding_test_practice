from ast import operator
import sys
from itertools import permutations 
from collections import deque
N = int(sys.stdin.readline())

data = list(map(int,sys.stdin.readline().split()))

oo = list(map(int,sys.stdin.readline().split()))
op = []
for i in range(4):
    for j in range(oo[i]):
        op.append(i)

random_op = list(permutations(op,len(op)))
print(op)
print(random_op)
ans = []
q = deque()
for tu in range(random_op):
    for i in range(len(data)):
        q.append(data[i])
    first = True
    temp = 0
    for j in tu :
        if first :
            a = q.popleft()
            b = q.popleft()
            if j == 0 :
                temp = a+b
            elif j == 1:
                temp = a-b 
            elif j == 2 :
                temp = a*b
            else :
                if b < 0 :
                    temp =  -1 * (a // abs(b))
                else :
                    temp = a//b
            key = False
        else :
            b = q.popleft()
            if j == 0 :
                temp = temp+b
            elif j == 1:
                temp = temp-b 
            elif j == 2 :
                temp = temp*b
            else :
                if b < 0 :
                    temp =  -1 * (temp // abs(b))
                else :
                    temp = temp//b
    ans.append(temp)

print(max(ans))
print(min(ans))
            