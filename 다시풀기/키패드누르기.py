numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
answer = ""
# pad = [["1","2","3"],["4","5","6"],["7","8","9"],["*","0","*"]]
pad = {"1":(0,0),
       "2":(0,1),
       "3":(0,2),
       "4":(1,0),
       "5":(1,1),
       "6":(1,2),
       "7":(2,0),
       "8":(2,1),
       "9":(2,2),
       "0":(3,1)}

left = (3,0)
right = (3,2)

while numbers :
    key=str(numbers.pop(0))
    if key == "1" or key == "4" or key == "7" :
        left = pad[key]
        answer += "L"
    elif  key == "3" or key == "6" or key == "9" :
        right = pad[key]
        answer += "R"
    else :
        location = pad[key]
        left_dist = abs(left[0]-location[0])+abs(left[1]-location[1])
        right_dist = abs(right[0]-location[0])+abs(right[1]-location[1])   
        
        if left_dist>right_dist :
            right = location 
            answer += "R" 
        elif right_dist>left_dist :
            left = location 
            answer += "L"
        else :
            if hand == "left":
                left = location
                answer += "L"
            else:
                right = location 
                answer += "R"                

print(answer)                