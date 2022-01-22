from itertools import permutations
numbers = "17"

def is_prime_number(x):
    # 2부터 (x - 1)까지의 모든 수를 확인하며
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False # 소수가 아님
    return True # 소수임

    
def solution(numbers):
    visit = [False]*10000000
    size = len(numbers)
    go = list(numbers)
    # print(go)
    count = 0
    for i in range(1,size+1):
        gogo = list(permutations(go,i))
        for i in range(len(gogo)):
            answer = "".join(gogo[i])
            if not visit[int(answer)] and not int(answer) == 0 and not int(answer) == 1 :
                if is_prime_number(int(answer)) :
                    visit[int(answer)]=True
                    count +=1 
                    
    # for i in range(len(go)):
    #     if not visit[int(go[i])] and not int(go[i]) == 0 and not int(go[i]) == 1:
    #         if is_prime_number(int(go[i])) :
    #             visit[int(go[i])]=True
    #             count +=1 
                
    # if size >=2 :
    #     for i in range(2,size+1):
    #         gogo = list(permutations(go,i))
    #         for i in range(len(gogo)):
    #             answer = "".join(gogo[i])
    #             if not visit[int(answer)] and not int(answer) == 0 and not int(answer) == 1 :
    #                 if is_prime_number(int(answer)) :
    #                     visit[int(answer)]=True
    #                     count +=1 
    #         #     print(answer)
    #         # print(gogo)
    #     answer = 0
    print(count)
    return count
solution(numbers)