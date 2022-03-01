lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

def solution(lines):
    answer = 0
    traffic = []
    # 시간을 ms 단위로 고쳐서 list에 start와 end를 넣는다.
    for line in lines :
        data = line.split(" ")
        hour , minute , second , ms = int(data[1][0:2]) , int(data[1][3:5]) , int(data[1][6:8]), int(data[1][9:])
        total = hour*3600*1000 + minute * 60 *1000 + second * 1000 + ms
        minus = ''
        for w in data[2] :
            if w == 's':
                break
            else:
                minus += w
        minus = float(minus)*1000
        # print(minus)
        # print(total)
        # print(total-(minus-1))
        start = total-(minus-1)
        end = float(total)
        traffic.append((start,end))
    
    for i in range(len(traffic)) :
        count_start = 0
        count_end = 0
        start = traffic[i][0]
        end = traffic[i][1]
        for j in range(len(traffic)):
            target_start = traffic[j][0]
            target_end = traffic[j][1]
            
            if start <= target_start < start+1000 :
                count_start +=1
            elif start <= target_end < start+1000 :
                count_start +=1
            elif target_start < start and target_end > start+1000 :
                count_start +=1
            
            if end <= target_start < end+1000 :
                count_end +=1
            elif end <= target_end < end+1000 :
                count_end +=1
            elif target_start < end and target_end > end+1000 :
                count_end +=1
            
            answer = max(answer,max(count_start,count_end))
    # print(traffic)
    # print(answer)
    return answer

solution(lines)