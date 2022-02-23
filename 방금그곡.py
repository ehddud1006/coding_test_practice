m = "ABCDEFG"
musicinfos = ["11:58,12:14,HELLO1,CDEFGAB","11:58,12:14,HELLO,CDEFGHAB", "11:58,12:20,HELLO2,CDEFGAB" ,"13:00,13:05,WORLD,ABCDEF"]
def solution(m, musicinfos):
    answer = ''
    ans =[]
    go = []
    for w in m :
        if w == "#":
            a = go.pop()
            if a == "A":
                go.append("H")
            if a == "C":
                go.append("I")
            if a == "D":
                go.append("J")
            if a == "F":
                go.append("K")
            if a == "G":
                go.append("L")
        else :
            go.append(w) 
    ma = "".join(go)
    print(ma)
    for w in musicinfos :
        data = w.split(",")
        if data[1][:2] == data[0][:2]:
            l = int(data[1][3:]) -int(data[0][3:]) 
        else :
            l =  (int(data[1][3:])+(int(data[1][:2]) - int(data[0][:2]))*60 ) -int(data[0][3:])
        gogo = []
        go = []
        for w in data[3] :
            if w == "#":
                a = go.pop()
                if a == "A":
                    go.append("H")
                if a == "C":
                    go.append("I")
                if a == "D":
                    go.append("J")
                if a == "F":
                    go.append("K")
                if a == "G":
                    go.append("L")
            else :
                go.append(w) 
        music = "".join(go) 
        leng = len(music) 
        for i in range(l):
            gogo.append(music[i%leng])
        key = "".join(gogo)
        if ma in key :
              ans.append((l,data[2]))
    ans.sort(key=lambda x:-x[0])
    print(ans)
        # print(l)
        # for i in range(len(data)):
            
        # print(data)
    
    if len(ans)==0:
        answer = "(None)"
    else :    
        answer=ans[0][1]
    return answer


solution(m,musicinfos)