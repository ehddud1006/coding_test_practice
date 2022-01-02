import sys
while True:
    a = int(input())
    merry_odd=0
    merry_even =0
    john_odd=0
    john_even =0
    if a == 0:   
        break
    else:
        merry = list(map(int,input().split()))
        john = list(map(int,input().split()))
        for i in merry:
            if i % 2 ==0:
                merry_even +=1
            else:
                merry_odd += 1
        
        for i in john:
            if i % 2 ==0:
                john_even += 1
            else:
                john_odd  += 1

        print(abs(merry_even-john_odd)) 
        # 설명에는 메리의 짝수 <->존의 홀수
        # 메리의 홀수 <->존의 짝수 으로 매칭 한다고 했는데,
        # 결국 메리의 짝수 <->존의 홀수 과
        # 메리의 홀수 <->존의 짝수 매칭되어 뺀값이 같으므로 하나만 구함.
        

    