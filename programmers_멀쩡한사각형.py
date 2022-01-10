import math
def solution(w,h):

    answer = 1
    a = math.gcd(w,h)
    
    break_square = (w/a+h/a-1)*a 
    square = w * h
    answer= square - break_square

    
    return answer