citations = [3, 0, 6, 1, 5]
def solution(citations):
    answer = 0
    
    mmax = max(citations)
    for i in range(0,mmax+1):
        count = 0
        a_count = 0
        for j in range(len(citations)):
            if citations[j]<=i :
                count +=1
        
        if count>=i :
            answer = i
                
    print(answer)
    return answer

solution(citations)