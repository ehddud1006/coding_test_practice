from itertools import permutations
k=80
dungeons=[[80,20],[50,40],[30,10]]
def solution(k, dungeons):
    answer = -1
    random = []
    for i in range(len(dungeons)):
        random.append(i)
    
    realrandom = list(permutations(random,len(dungeons)))
    # print(realrandom)
    for tuple in realrandom:
        count = 0
        copy_k =k
        for i in tuple :
            if copy_k>=dungeons[i][0] :
                copy_k -= dungeons[i][1]
                count +=1
            else :
                break
        if answer < count :
            answer = count 
    
    # print(answer)          
    return answer

solution(k,dungeons)