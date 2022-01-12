lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
win = {i:1 for i in win_nums}
answer = []
print(win)

count = 0
zero_count = 0
for i in range(len(lottos)) :
    if lottos[i] == 0 :
        zero_count += 1
    if lottos[i] in win :
        count += 1

max = count + zero_count
min = count 

answer.append(rank[max])
answer.append(rank[min])
print(count)