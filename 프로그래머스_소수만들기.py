from itertools import combinations


nums = [1,2,3,4]

def is_prime(num):
    for i in range(2,num) :
        if num % i == 0:
            return False
    return True    

arr = list(combinations(nums,3))
answer = 0
for n1,n2,n3 in arr :
    sum = 0
    sum = n1+n2+n3 
    if is_prime(sum) :
        answer += 1
 
print(answer)   
        
    