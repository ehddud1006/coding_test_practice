n=78
def solution(n):
    answer = 0
    init = 0
    for w in bin(n)[2:]:
        if w == '1':
            init+=1
    n+=1
    while n<1000001 :
        target = 0
        for w in bin(n)[2:]:
            if w == '1':
                target+=1
        if target == init :
            answer = n
            break
        n+=1
    return answer

solution(n)