numbers = [1, 1, 1, 1, 1]
target = 3
global count
count = 0
def dfs(limit,sum,numbers,target) :
    global count
    if limit == len(numbers) :
        if target == sum :
            count +=1
        return 
    
    dfs(limit+1,sum+numbers[limit],numbers,target)
    dfs(limit+1,sum-numbers[limit],numbers,target)

def solution(numbers, target):
    dfs(0,0,numbers,target)
    return count

a = solution(numbers, target)  
print(a)
    

    