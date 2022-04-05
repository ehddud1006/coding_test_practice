from itertools import permutations

def solution(n, weak, dist):
    
    results = []
    
    # weak를 기준으로 기준점 이동
    for w in weak:
        
        # weak 기준점을 기준으로 weak 초기화
        weak_initialization = []
        for j in range(len(weak)):
            weak_init = weak[j] - w
            if weak_init < 0:
                weak_init += n
                weak_initialization.append(weak_init)
            else:
                weak_initialization.append(weak_init)
        
        # dist 순열을 바탕으로 모든 weak을 cover할 수 있는 인원 수 세기
        max_weak = max(weak_initialization)
        for dist_perm in permutations(dist): # 거리 조합 생성
            cnt = 1
            location = 0
            for d in dist_perm:
                location += d
            if location < max_weak: # 모든 weak을 cover 하지 못했다면
                cnt += 1
                # 현재보다 멀리 있는 weak 중에서 가장 가까운 지점으로 location update
                location = min([w for w in weak_initialization if w > location])
            else:
                results.append(cnt)
                break
                    
    return min(results) if results else -1