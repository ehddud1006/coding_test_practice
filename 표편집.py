n = 8
k = 2
cmd = 	["C","D 1","C","U 1","C","Z"]

def solution(n, k, cmd):
    answer = ''
    cursor = k
    commands = cmd
    dic = {}
    delete_save = ['O']*n
    stack = []
    # 리스트를 만든다. 
    # 1행의 일경우 [0,2]이렇게 그 전행의 정보와 다음행의 정보를 만든다.
    for i in range(n):
        dic[i]=[i-1,i+1]
    dic[0]=[None,1]
    dic[n-1]=[n-2,None]
    
    for command in commands :
        if len(command) != 1 :
            char, move = command.split()
            for _ in range(int(move)):
                if char == "D" :
                    cursor = dic[cursor][1]
                else :
                    cursor = dic[cursor][0]
        else :
            if command == "C" :
                delete_save[cursor]='X'
                stack.append(cursor)
                prev, next = dic[cursor]
                if dic[cursor][1]==None :
                    dic[prev]=[dic[prev][0],None]
                    cursor = prev
                elif dic[cursor][0]==None  :
                    dic[next]=[None,dic[next][1]]
                    cursor = next
                else :
                    dic[prev]=[dic[prev][0],next]
                    dic[next]=[prev,dic[next][1]]
                    cursor=next
            else :
                live = stack.pop()
                delete_save[live]='O'
                prev, next = dic[live]
                if prev != None:
                    dic[prev]=[dic[prev][0],live]
                if next != None:
                    dic[next]=[live,dic[next][1]]
              
    print(dic)
    print(''.join(delete_save))
    answer = ''.join(delete_save)
    return answer

solution(n,k,cmd)