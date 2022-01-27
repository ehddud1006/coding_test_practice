import sys
input = sys.stdin.readline
# 문자열의 경우 realine을 사용하면 마지막의 개행문자까지 입력되므로
# rstrip()을 사용해서 제거해주어야한다.
enemy = input().rstrip()

strr = ''
ans = ''
tag = False
# # 총 6개의 case가 존재한다.
# 1. 태그가 아닌 공백이 나올때. -> 기존의 strr 과 " "를 더한 값을 ans의 뒤에 붙힌다.그리고 strr 초기화.
# 2. 태그 시작일때 -> tag = True로 태그가 시작임을 알린다. 기존에 저장되어있던 strr을 ans에 
#                     붙히고, strr = "<"로 변경
# 3  태그가 끝날때 -> tag = False로 변경하고 ">"을 strr 뒤에더해 ans에 붙힌다. 그리고 strr초기화
# 4. 태그= True인 상태에서 숫자 , 알파벳이 나올때 그냥 strr 뒤에 붙힌다.
# 5. 태그가 아닐때 숫자나 알파벳이 나올때 -> strr의 앞에 붙힌다
for w in enemy :
    #1
    if w == " " and not tag:
        ans += strr + " "
        strr =""
    #2
    elif w == "<" :
        tag = True
        ans += strr 
        strr = "<"
    #3
    elif w == ">" :
        tag = False
        strr = strr + w
        ans += strr 
        strr = ""
    #4    
    elif tag :
        strr = strr+w
    #5    
    else :
        strr = w+strr
        
ans = ans + strr
print(ans)
    
    