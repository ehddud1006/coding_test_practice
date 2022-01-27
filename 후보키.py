from itertools import combinations

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    answer = 0
    
    row = len(relation)
    col = len(relation[0])
    print(row)
    print(col)
    num =[]
    for i in range(col):
        num.append(i)
    for i in range(1,col+1):
        random = list(combinations(num,i))
        print(random)
        
        dic = {}
        for j in range(row):
            if i == 1 :
                if relation[j][random[j][0]] in dic :
                    dic[relation[j][random[j][0]]] +=1
                else :
                    dic[relation[j][random[j][0]]] =1
                
            
    return answer

solution(relation)