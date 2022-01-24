global count 
count = 0
numbers = [1, 1, 1, 1, 1]
target = 3
def dfs(depth,ans,numbers,target):
    global count
    if depth >=5:
        if ans == target :
            count +=1
        return
    
    dfs(depth+1,ans-numbers[depth],numbers,target)
    dfs(depth+1,ans+numbers[depth],numbers,target)
def solution(numbers, target):
    dfs(0,0,numbers,target)
    print(count)
    return count

solution(numbers,target)


