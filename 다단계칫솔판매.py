enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
seller = ["young", "john", "tod", "emily", "mary"]
amount = [12, 4, 2, 5, 10]

def solution(enroll, referral, seller, amount):
    idx_parent = dict() 
    results =[ 0 for i in range(len(enroll))]
    # 사원들의 idx번호와 부모정보 하나에 저장.
    # 사원명이 모두 string이라 딕셔너리로 해싱해둠.
    for idx, person in enumerate(enroll):
        idx_parent[person] = [idx, referral[idx]]

    # seller를 어떻게 처리해줘야 하나.. 
    # 문제 설명대로 10만의 쿼리를 일일이 해주면 터질거같은데
    # seller를 정리해서 한번에 싹 올려주는건..? 일단 이렇게 짜자
    for i in range(len(seller)):
        idx_parent[seller[i]].append(amount[i]*100)

    #각 사원들의 판매실적 처리
    for k,v in idx_parent.items():
        #판매실적이 없을 수 있으니까.
        if len(v) <=2:
            continue
        queries = [0]*5 # 금액과 얼마나 부모를 타고올라가야하는지 count값 저장
        moneys = v[2:]
        for money in moneys:
            tmp = money
            count = 0
            while tmp != 0:
                c= tmp -int(tmp * 0.1)
                queries[count] += c
                tmp //= 10
                count += 1

        person = idx_parent[k][0]
        for query in queries:
            if query == 0:
                break
            else:
                results[person] += query #해당 쿼리 값을 더해주고
                person_name = idx_parent[enroll[person]][1] # 부모로 포인터를 변경함
                if person_name == '-':
                    break
                else:
                    person = idx_parent[person_name][0]
    return results

solution(enroll, referral, seller, amount)