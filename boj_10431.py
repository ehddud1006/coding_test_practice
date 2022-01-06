import sys

input = sys.stdin.readline
N = int(input())
ans = []


for i in range(N):
    line = list(map(int,input().split()))
    line.pop(0)
    Slist = []
    step = 0
    # 제일앞 원소 제거
    # print(line)
    
    for j in range(20) :
        Slist.append(line[j])
        Slist.sort()
        for k in range(j+1) :
            if(Slist[k]==line[j]) :
                step += j-k
                break
    ans.append(step)

for i in range(N):
    print(f'{i+1} {ans[i]}')