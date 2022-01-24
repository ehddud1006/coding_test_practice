answers = [1,2,3,4,5]
supo1 = [1,2,3,4,5]
supo2 = [2,1,2,3,2,4,2,5]
supo3 = [3,3,1,1,2,2,4,4,5,5]
def solution(answers):
    answer= []
    count = [0]*3
    for i in range(len(answers)):
        if answers[i] == supo1[i%5] :
            count[0] +=1 
        if answers[i] == supo2[i%8] :
            count[1] +=1
        if answers[i] == supo3[i%10] :
            count[2] +=1
    maxa = max(count)
    for i in range(3):
        if maxa == count[i] :
            answer.append(i+1)

    
    
    print(answer)
   
    return answer

solution(answers)