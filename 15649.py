n,m = map(int,input().split())

# 백트레킹은 dfs로 조건을 주어서 구하는 것.
# 파이썬에서는 permutations를 사용가능함.

s=[]
def dfs():
    if len(s)==m:
        print(' '.join(s))
        return
    
    for i in range(1,n+1):
        if str(i) not in s:
            s.append(str(i))
            dfs()
            s.pop()

dfs()

# import sys
# input = sys.stdin.readline
# from itertools import permutations

# m, n = map(int, input().split())
# lst = [i+1 for i in range(m)]

# c_lst = list(permutations(lst,n))
# for i in c_lst:
#     for j in i:
#         print(j, end=' ')
#     print('')
    