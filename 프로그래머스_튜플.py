s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

def solution(s):
    dic = {}
    answer = []
    s = s[1:-1]
    s = s[1:-1]
    s = s.split("},{")
    print(s)
    s.sort(key=len)
    print(s)
    for word in s :
        k = word.split(",")
        for w in k :
            if w in dic :
                dic[w]+=1
            else :
                dic[w]=1
    dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    # print(dic)
    for key , value in dic:
        answer.append(int(key))
    
    # print(new_s.split(","))
    # arr = s.split(",")
    # for sss in arr :
    #     print(sss[1:-1])
    print(answer)
    
    return answer

solution(s)