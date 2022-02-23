from calendar import c
import math
fees =[180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
def solution(fees, records):
    answer = []
    dic = {}
    Money = {}
    Nu = {}
    # test = "00:34"
    # print(int(test[:2]))
    # print(test[3:5])
    for record in records :
        time , carN , ttype = list(record.split())
        if ttype == "IN":
            dic[carN]=time
        else :
            # print(ttype)
            out_hour = int(time[:2])
            out_minute = int(time[3:5])
            out = out_hour*60 + out_minute
            # print(dic[carN])
            # print(dic[carN][:2])
            hour = int(dic[carN][:2])
            minute = int(dic[carN][3:5])
            dic[carN]="0"
            iin = hour*60 + minute
            
            total = 0
            gap = out - iin 
           
            if carN in Nu :
                Nu[carN]+=gap
            else :
                Nu[carN]=gap
            # if gap<= fees[0]:
            #     total = fees[1]
            # else:
            #     total = fees[1] + (math.ceil((gap-fees[0]/fees[2]))*fees[3]) 
            
            # if carN in Money :
            #     Money[carN]+=total
            # else :
            #     Money[carN]=total
    
    for key, value in dic.items():
        if value != "0" :
            hour = int(dic[key][:2])
            minute = int(dic[key][3:5])
            iin = hour*60 + minute
            gap = 1439 - iin
            
            if key in Nu :
                Nu[key]+=gap
            else :
                Nu[key]=gap
            # if gap<= fees[0]:
            #         total = fees[1]
            # else:
            #     total = fees[1] + (math.ceil((gap-fees[0]/fees[2]))*fees[3]) 
            
            # if key in Money :
            #     Money[key]+=total
            # else :
            #     Money[key]=total
    d1 = sorted(Nu.items())
    for key, value in d1:
        total = 0
        if value<= fees[0]:
            total = fees[1]
        else:
            # print(math.ceil(1/60))
            # print(((value-fees[0])//fees[2]))
            total = fees[1] + (math.ceil(((value-fees[0])/fees[2]))*fees[3]) 
        
        # if carN in Money :
        #     Money[carN]+=total
        # else :
        #     Money[carN]=total
        answer.append(total)
    # print(answer)
    return answer

solution(fees,records)