jobs = [[0, 3], [1, 9], [2, 6]]
import heapq

def solution(jobs):
    answer = 0
    original_length = len(jobs)
    jobs.sort()
    heap = []
    now = 0
    step = 0
    
    # 처음에는 아래와 같이 _ 를 사용해서 original_length 만큼
    # for문을 돌려주려고 했지만, 제가 간과했던 것은 처리할 프로세스가
    # 없을 경우를 고려하지 않았습니다. 그러므로 아래의 for문을
    # 사용할 수 없었습니다.
    # for _ in range(original_length):
    
    # 위와 같은 이유로 인해 process를 처리할 경우에만 step을 
    # 증가시켜줍니다. 
    while step < original_length : 
        # count 변수는 heap에 들어가는 프로세스의 갯수만큼 
        # jobs 리스트를 pop 시켜주기 위해서 선언하였습니다.
        count = 0
        # 현재 시간보다 process가 들어온 시간이 적거나 같다면 
        # 그 프로세스를 heap에 넣어주는데 여기서 중요한점은 
        # 시작시간, 수행시간 => 수행시간 , 시작시간으로 바꾸어넣어줍니다.
        # 그 이유는 heap의 정렬이 첫번째 원소를 기준으로 되기 때문이고,
        # 우리는 가장 빨리 끝내는 프로세스부터 쳐내서 좋은 효율을 만들어
        # 내야합니다.
        for i in range(len(jobs)):
            if jobs[i][0] <= now :
                heapq.heappush(heap,[jobs[i][1], jobs[i][0]])
                count +=1
        
        # 위에서 말씀드린대로, heap에 들어가는 프로세스의 수만큼
        # jobs에서 pop을 해줍니다. pop(0)를 사용한 이유는 jobs의
        # 최대갯수가 500인지라 큰 영향을 주지 않을 것이라고 판단하여
        # deque를 사용하지 않았습니다.        
        for i in range(count):
            jobs.pop(0)
        
        # heap에 처리해야할 프로세스가 존재한다면 꺼내어
        # 수행시간 만큼 현재시간에서 더해주고,
        # answer 에는 현재시간 - process 가 들어온 시간을 빼줍니다.
        # answer += now - process[1] 인 이유는 
        # 처리되기 위해 , 대기한 시간까지 고려해야하기 때문입니다.
        # 그리고 처리가 된 경우에만 step을 증가시켜줍니다.
        if heap : 
            process = heapq.heappop(heap)
            now += process[0]
            answer += now - process[1]
            step+=1
        # 처리할 process가 없을경우에 시간을 1초증가시켜줍니다.
        else :
            now += 1
            
    return answer // original_length

solution(jobs)