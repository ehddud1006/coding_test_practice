progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
days = 1
count = 0
answer = []
while progresses:
        if 100 <= progresses[0]+speeds[0]*days :
            count += 1 
            progresses.pop(0)
            speeds.pop(0)
            #  progresses.pop() 을 수행할 경우에는 
            # [93, 30, 55] 에서 55가 pop 되었다.
            # pop(0)로 첫번째 인덱스가 pop되게 해주어야한다.
        elif count > 0  :
            answer.append(count)
            count = 0
        else:
            days+=1   
answer.append(count)            
print(answer)
