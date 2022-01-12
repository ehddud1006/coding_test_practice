n=45

mok = 1
na = 1
answer= ''
while mok != 0 :
    mok = n//3
    na = n%3 
    
    answer = answer + str(na) 
    n = mok

print(int(answer,3))