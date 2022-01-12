absolutes = [4,7,12]
signs = [True,False,True]
answer =0
for i in range(len(absolutes)):
    if signs[i] :
        answer += absolutes[i]
    else :
        answer -= absolutes[i]   

