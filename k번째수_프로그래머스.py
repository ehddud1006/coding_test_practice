array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

answer= []
# for i in array:
#     string += str(i)
while commands :
    list = []
    i,j,k = commands.pop(0)
    for a in range(i-1,j):
        list.append(array[a])
    list.sort()  
    answer.append(list[k-1])

print(answer)