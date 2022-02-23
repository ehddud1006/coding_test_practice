files =  ["img000012345.png", "img1.png", "img2", "iMG02"]
NUM = ["1","2","3","4","5","6","7","8","9","0"]
ALPHA =["A","B","C","D","E","F","G","H","I","J","K"
           ,"L","M","N","O","P","Q","R","S","T","U"
           ,"V","W","X","Y","Z","-","a","b","c","d","e","f","g","h","i","j","k"
           ,"l","m","n","o","p","q","r","s","t","u"
           ,"v","w","x","y","z"]
def solution(files):
    answer = []
    ans = []
    index = 0
    # print(int("0010"))
    # head = ["0"]
    # hhead="".join(head)
    # print(hhead)
    for file in files :
        head=[]
        Number = []
        key = True
        count = 1
        for w in file :
            if key and w in ALPHA :
                head.append(w)
            elif w in NUM and count <= 5:
                key = False
                count +=1
                Number.append(w)
            else : 
                break
        hhead = "".join(head)
        NNumber = "".join(Number)
        ans.append((hhead.upper(),int(NNumber),index))
        index +=1
    ans.sort(key=lambda x:(x[0],x[1]))
    for a,b,c in ans :
        # print(f'{a} {b} {c}')
        answer.append(files[c])
    print(answer)
    return answer

solution(files)