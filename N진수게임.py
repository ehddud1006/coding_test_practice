n=2
t=4
m=2
p=1
dic = {0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7"
        ,8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E"
        ,15:"F"}

def solution(n, t, m, p):
    answer = ''
    go = t*m*p
    strr = ''
    
    target =0
    count = 0
    while True :
        mok=1
        na=1
        big = target
        ans = ''
        while mok  :
            mok = big//n
            na = big%n
        
            ans = dic[na]+ ans
            big = mok
        count += len(ans)
        strr += ans
        if count >= go :
            break
        target+=1
        
    for i in range(t):
        answer+=strr[(p-1)+(m*i)]
    # print(strr)
    # print(answer)  
        
    
    # print(bin(1))
    # if n == 2:
    #     for i in range(0,go):
    #         strr += bin(i)[2:]
    #     for i in range(t):
    #         answer+=strr[(p-1)+(m*i)]
    # if n == 8:
    #     for i in range(0,go):
    #         strr += oct(i)[2:]
    #     for i in range(t):
    #         answer+=strr[(p-1)+(m*i)]
    # if n == 16:
    #     for i in range(0,go):
    #         strr += hex(i)[2:]
    #     for i in range(t):
    #         answer+=strr[(p-1)+(m*i)]
    # print(answer)
    return answer

solution(n,t,m,p)