numbers = [1,2,3,4,6,7,8,0]

answer = 0
frame = [False]*10
for i in range(len(numbers)) :
    frame[numbers[i]]=True

for i in range(len(frame)) :
    if frame[i] == False :
        answer += i

print(answer)