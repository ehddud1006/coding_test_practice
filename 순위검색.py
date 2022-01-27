info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
def solution(info, query):
    answer = []
    for qu in query :
        query_split = qu.split()
        print(query_split)
        mid_ans = 0
        for w in info :
            info_split = w.split()
            if int(query_split[-1]) > int(info_split[-1]) :
                continue
            count = 0
            for i in range(0,7,2):
                if query_split[i]=='-' :
                    count +=1
                    continue
                else :
                    if info_split[i//2] == query_split[i] :
                        count +=1
                    else :
                        break
            if count == 4:
                mid_ans += 1
        answer.append(mid_ans)        
            
    print(answer)
    return answer

solution(info,query)