brown = 10
yellow = 2
def solution(brown, yellow):
    total = brown + yellow
    answer = []
    for i in range(1,yellow+1):
        if yellow % i == 0 :
            j = yellow//i
        if (i * j) + (2*(i+j)+4) == total :
            if i > j:
                answer.append(i)
                answer.append(j)
            else :
                answer.append(j)
                answer.append(i)
            break
    print(answer)
    return answer

solution(brown,yellow)