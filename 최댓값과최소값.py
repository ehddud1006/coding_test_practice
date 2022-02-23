s = "1 2 3 4"
def solution(s):
    answer = ''
    go = []
    data = list(map(int,s.split()))
    go.append(str(min(data)))
    go.append(str(max(data)))
    answer = " ".join(go)
    print(answer)
    return answer

solution(s)