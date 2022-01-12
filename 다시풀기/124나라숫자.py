n = 5

mok = 1
na = 1
answer = ''
dict = {1:"1",2:"2",0:"4"}

while mok  :
    mok = n//3
    na = n%3 
    
    if na == 0 :
        mok -= 1
    answer = dict[na] + answer
    
    n = mok

print(answer)      
    
    