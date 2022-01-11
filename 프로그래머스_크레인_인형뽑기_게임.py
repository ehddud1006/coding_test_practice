board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,1,5,5,3]
basket = []
top = 0
answer = 0
# print(len(board))
# 2차원 배열의 경우 row의 길이가 출력된다.
while moves :
    action = moves.pop(0)
    for i in range(len(board)):
        if board[i][action-1] != 0:
            if top == board[i][action-1] :
                answer = answer + 2
                basket.pop()
                if len(basket)>=1 :
                    top = basket[-1]
                else :
                    top = 0   
                   
            else:          
                basket.append(board[i][action-1])
                top = board[i][action-1]
            
            board[i][action-1] = 0   
            break
    
print(answer)
    