n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

# https://roomedia.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B7%B8%EB%9E%98%ED%94%84-Floyd-Warshall-Level3

def solution(n, results):
    answer = 0
    graph = [[None]*(n+1) for _ in range(n+1)]
    for result in results :
        win , lose = result[0] , result[1]
        graph[win][lose] = True
        graph[lose][win] = False
    
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            if j == i :
                continue
            for k in range(1, n+1):
                if graph[j][i] == graph[i][k] and not graph[j][i] == None :
                    graph[j][k]=graph[j][i]
                    graph[k][j]= not graph[j][i]
    
    for i in range(1,n+1):
        count = 0
        for j in range(1,n+1):
            if graph[i][j] == None :
                count +=1
        if count == 1 :
            answer +=1 
    
    # print(answer)
    return answer

solution(n,results)