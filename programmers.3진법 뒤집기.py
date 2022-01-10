def solution(n):
    mok = 1
    na = 1

    answer=''
    while n!=0 :
        mok = n//3
        na = n % 3
        answer += str(na)
        # if mok<3 :
        #     answer += str(mok)
        #     break
        # 테스트 케이스 1번이 계속 안되어서 
        # if문을 제거하고 다른분의 풀이를 참고하였다.
        # if문에서 문제가 생긴거 같고 , 그전은 while True 였다.
        n=mok
    
    # print(int(answer, 3))
    # int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌


    return int(answer, 3)