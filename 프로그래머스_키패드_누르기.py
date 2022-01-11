numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	
hand = "left"
answer=''
# phone = [[0]*3 for _ in range(4)]
go = ['1','2','3','4','5','6','7','8','9','*','0','#']
key_location = {'1':(0,0),
                '2':(0,1),
                '3':(0,2),
                '4':(1,0),
                '5':(1,1),
                '6':(1,2),
                '7':(2,0),
                '8':(2,1),
                '9':(2,2),
                '*':(3,0),
                '0':(3,1),
                '#':(3,2)}
# leftx = 0
# lefty = 0

left = (3,0)
right = (3,2)

# for i in range(4):
#     for j in range(3):
#         phone[i][j]=go[i*3+j]
        
# for i in range(4):
#     for j in range(3):
#         print(f'{phone[i][j]}',end=' ')
#     print()            

while numbers :
    key = numbers.pop(0)
    if key == 1 or key == 4 or key == 7:
        location = key_location[str(key)]
        left = location
        answer+="L"
    elif key == 3 or key == 6 or key == 9:    
        location = key_location[str(key)]
        right = location
        answer+="R"
    else:    
        location = key_location[str(key)]
        left_dist = abs(location[0]-left[0])+abs(location[1]-left[1])
        right_dist = abs(location[0]-right[0])+abs(location[1]-right[1])
        if left_dist>right_dist :
            right = location
            answer+="R"
        elif left_dist<right_dist :
            left = location
            answer+="L"
        else :
            if hand == "right" :
                right = location
                answer+="R"
            else :
                left = location
                answer+="L"

print(answer)                       

