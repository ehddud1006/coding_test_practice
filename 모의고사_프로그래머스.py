# 12345 12345 12345
# 21232425 2123   2425
# 01234567 891011  12131415

# 3311224455  3311224455
# 0123456789  10
supo2 = [2,1,2,3,2,4,2,5]
supo3 = [3,3,1,1,2,2,4,4,5,5]
import copy 

answers = [4,4,1,1,1,3,4,5]
answers2 = copy.deepcopy(answers)
answers3 = copy.deepcopy(answers)

index = 1
count1 = 0
count2 =0
count3 = 0
while answers :
    if index%5 == answers.pop(0) % 5 :
        count1 +=1
    index += 1
    
index = 0
print(answers2)
while answers2 :
    if supo2[index % 8] == answers2.pop(0) :
        count2+=1
    index +=1    
    

index = 0               
while answers3 :
    if supo3[index % 10] == answers3.pop(0) :
        count3+=1
    index +=1    

print(count1)
print(count2)
print(count3)

answer = []
answer.append((1,count1))
answer.append((2,count2))
answer.append((3,count3))
answer.sort(key=lambda x: (-x[1],x[0]))
print(answer)
boss = []
prev = answer[0][1]
for i ,j in answer :
    if prev == j:
        boss.append(i)
print(boss)
