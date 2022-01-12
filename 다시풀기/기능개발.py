progresses = [93, 30, 55]
speeds = [1, 30, 5]

day = 1
count = 0
answer = []
while progresses :
    if progresses[0] + speeds[0] * day >= 100 :
        progresses.pop(0)
        speeds.pop(0)
        count+= 1
    else :
        day += 1
        if count > 0 :
            answer.append(count)
            count = 0
answer.append(count)

print(answer)