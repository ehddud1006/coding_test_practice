from collections import deque

def solution(record):
    answer = []
    command = deque()
    user = deque()
    dic = {}
    for word in record:
        data = word.split()
        # print(data)
        if data[0]=='Enter' :
            command.append(data[0])
            user.append(data[1])
            dic[data[1]]=data[2]
        elif data[0]=='Leave' :
            command.append(data[0])
            user.append(data[1])
        else :
            if user[1] in dic :
                del(dic[user[1]])
                dic[data[1]]=data[2]
    
    while command :
        com = command.popleft()
        us = user.popleft()
        ans = ''
        if com=='Enter':
            ans = dic[us]+"님이 들어왔습니다."
        else :
            ans = dic[us]+"님이 나갔습니다."
        answer.append(ans)
    return answer

# solution(record)