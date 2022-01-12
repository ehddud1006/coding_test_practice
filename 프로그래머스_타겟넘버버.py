
def dfs(n,limit,sum,numbers,target) :
    global count 

    if n == limit :
        if sum==target:
            count +=1
            return
    else :
        dfs(n,limit+1,sum+numbers[limit],numbers,target)
        dfs(n,limit+1,sum-numbers[limit],numbers,target)

numbers = [1, 1, 1, 1, 1]
target = 3  

n = len(numbers)

dfs(n,0,0,numbers,target)

count = 0