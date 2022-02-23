arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr2)):
                temp +=arr1[i][k]*arr2[k][j]
            tmp.append(temp)
        answer.append(tmp)
    print(answer)
    return answer

solution(arr1,arr2)