s = "  aa bb  cc "
alpha ="abcdefghijklmnopqrstuvwxyz"
alpha2 = alpha+"abcdefghijklmnopqrstuvwxyz".upper()
def solution(s):
    data = list(s.split())
    print(data)
    ans = []
    for word in data :
        if word[0] in alpha2 :
            strr = word[0].upper() + word[1:].lower()
            ans.append(strr)
        else:
            ans.append(word.lower())
    print(ans)
    answer = ' '.join(ans)
    print(answer)
    return answer

solution(s)