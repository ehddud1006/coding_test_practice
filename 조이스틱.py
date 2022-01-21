name = "ABABAABA"

# # up = {'B':1,'B':1,}
# def solution(name):
#     answer = 0
#     # print(91-ord('Z'))
#     index = 0
#     cursor = 0
#     la = len(name)
#     for w in name :
#         if index != 0 and w !='A':
#             answer += min(index-cursor,la+cursor-index)
            
#             cursor = index
#         if w == 'A':
#             index+=1
#             continue
#         else :
#             answer+=min(ord(w)-ord('A'),91-ord(w))
        
#         index +=1
#     print(answer)
#     return answer

import math

def solution(name):
    answer = 0
    for i in range(len(name)):#상하먼저구하기
        x=ord(name[i])-ord("A")
        y=ord("Z")-ord(name[i])+1
        answer+=(x if x<y else y)

    tmp=0
    shift=len(name)-1
    for i in range(len(name)):
        if name[i]=="A":
            tmp=i
            while(tmp<len(name) and name[tmp]=="A"):
                tmp+=1
            left=(0 if i==0 else i-1)
            right=len(name)-tmp
            shift=min(shift,left+right+min(left,right))
    answer+=shift
    return answer

solution(name)