phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    dic = {}
    key = True
    for number in phone_book :
        dic[number]=1
    # print(dic)
    for name in dic :
        strr = ''
        # print(name)
        for w in name :
            strr += w 
            # print(strr)
            if strr in dic and name != strr:
                key = False
                answer=False
    if key :
        answer = True
    # print(answer)
    return answer

solution(phone_book)