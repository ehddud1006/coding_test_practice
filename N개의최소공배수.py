import math

arr = [2,6,8,14]

def solution(arr):
    answer = 0
    g = math.gcd(arr[0],arr[1])
    l = arr[0]*arr[1]/g
    for i in range(2,len(arr)):
        g = math.gcd(l,arr[i])
        l = l*arr[i]/g
    
    answer = l
    return answer