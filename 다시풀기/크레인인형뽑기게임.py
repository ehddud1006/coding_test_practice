board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
basket = []
answer = 0
while moves :
    crane  = moves.pop(0)-1
    doll = 0
    for i in range(len(board)) :
        if board[i][crane] != 0 :
            doll = board[i][crane]
            board[i][crane] = 0
            if len(basket)>0 and basket[-1] == doll :
                basket.pop()
                answer = answer + 2
            else :
                basket.append(doll)    
            break

print(answer)  
             
    