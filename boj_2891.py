N , R , B = list(map(int,input().split())) 
breakKayak = list(map(int,input().split()))
repairKayak = list(map(int,input().split()))
# 입출력
angel = []
# 카약을 빌려줄수 있는 팀 넘버

list = [0 for i in range(N+2)]
# 뒤에서 설명드리겠습니다



for i in breakKayak :
    list[i]=-1 

# 카약이 고장난팀 -1

for i in repairKayak :
    if list[i]==-1:
        list[i] =0
    else:
        list[i]= 1
        angel.append(i)

# 카약이 손상이 됐는데 여유분이 있을 수도 있으므로 
# 그 경우는 if로 구분하여 0 (이상없는 팀 (자기팀이 여유분을 사용))
# 으로 생각했습니다.
# 카약이 여유분이 있는 팀은 1로 두었습니다. 그리고 이팀들은
# angel 배열에 팀 넘버를 따로 모았습니다.




for k in angel : 
    # 아까 모아둔 angel팀 넘버입니다.
    if list[k-1] == -1 :
        list[k]=0
        list[k-1]=0
    elif list[k+1] == -1 :
        list[k]=0
        list[k+1]=0
    # 찐 으로 여유분이 있는 팀중 앞 뒤를 살펴서 -1(손상된 팀이 있다면)
    # 카약을 빌려주고 손상된 팀도 0으로 빌려준 팀도 0으로 바꿉니다.
    # list = [0 for i in range(N+2)]
    # N+2로 둔 이유는 기존 번호를 그대로 사용하고 싶기도 하고,
    # 앞순서 뒷순서를 고려해야하는데 마지막 번호 같은경우에는
    # 뒷순서가 없으므로 index error가 날 것이므로 여유분으로 +1을 
    # 더 주었습니다.
count = 0


for i in range(N+1):
    if list[i] == -1 :
        count+=1
# 최종적으로 출발하지 못한 팀을 카운트합니다.


print(count)