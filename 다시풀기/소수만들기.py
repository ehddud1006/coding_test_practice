from itertools import combinations

def is_prime(num) :
    for i in range(2,num) :
        if num%i == 0 :
            return False
    return True    

nums = [1,2,3,4]
arr = list(combinations(nums,3))
answer = 0
for x,y,z in arr  :
    sum = x+y+z 
    if is_prime(sum) :
        answer +=1
        
