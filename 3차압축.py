

msg = "KAKAO"
def solution(msg):
    answer = []
    dic = {"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11
           ,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21
           ,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    index = 27
    
    print(msg[0:0])  
    i = 0
    while i< len(msg):
        tmp = 0
        length = 0
        for j in range(i+1,len(msg)+1):
            if msg[i:j] in dic :
                length = len(msg[i:j])
                tmp = dic[msg[i:j]]
            else :
                dic[msg[i:j]]=index
                index +=1
                break
        i += length
        answer.append(tmp)
    print(answer)
    return answer

solution(msg)