skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
def solution(skill, skill_trees):
    answer = 0
    data = list(skill)
    for w in skill_trees:
        ddata = list(w)
        a = []
        for i in range(len(ddata)):
            if ddata[i] in data :
                a.append(ddata[i])
        key = True
        for i in range(len(a)):
            if a[i] != data[i]:
                key = False
                break
        if key :
            answer+=1
    
    # ak = "tatak"
    print(answer)  

solution(skill , skill_trees)