from audioop import reverse
from collections import deque

# *********************************************
# new.sort(key=lambda x :(-len(x[0]),x[1]))
# string을 비교하기위해서 len 을 사용하였고 -는 내림차순

# len은 길이라 틀린 값이였다.
#  new.sort(key=lambda x :(-int(x[0]),x[1]))
    
# 첫번째 원소가 같을 경우 두번째 원소를 비교한다.
# char의 경우 ord 를 사용하면 된다.
# *********************************************
numbers=[30,3021]	
def solution(numbers):
    nu =['33', '330', '34', '5', '9']
    new = []
    # ['9', '5', '34', '30', '3']
    # ['9', '5', '34', '33!', '30']
    # nu = ['6','10','2']
    nn = {}
    q = deque()
    for i in range(len(numbers)):
        strr = str(numbers[i])
        strr_len = len(strr)
        for i in range(4-strr_len):
            strr += strr[-1]
        new.append((strr,strr_len))
    # print(new)
    new.sort(key=lambda x :(-int(x[0]),x[1]))
    
    # print(new)
   
    answer = ''
    
    for a,b in new:
        answer+=a[:b]
    print(answer)
    return answer

solution(numbers)