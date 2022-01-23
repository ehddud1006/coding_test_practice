from itertools import combinations, permutations

# 문제 읽고 중요부분에 밑줄 긋기 
# 미리 구해놓으면 편한것? 미리 구해놓기.
# 이문제에서는 소수의 합으로 만들어질 수 있는 값
# 소수의 곲으로 만들어질수 있는 값.
# 파이썬 set은 데이터 순서가 없다.
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]
mmax = [0,9,99,999,9999,99999]


K,M = map(int,input().split())
prime = prime_list(mmax[K])

# print(prime)

count = 0
add = set()
mul = set()
for i in range(len(prime)):
    for j in range(i+1,len(prime)):
        go = prime[i]+prime[j]
        # if go == 22:
        #     # print("why")
        if go >= 10**K:
            break
     
        add.add(go)

for i in range(len(prime)):
    for j in range(len(prime)):
        go = prime[i]*prime[j]
        if go >= 10**K:
            break
     
        mul.add(go)
# print(add)
# print(mul)            
num_list = ['0','1','2','3','4','5','6','7','8','9']
# num_list = [str(i) for i in range(10)]
for case in permutations(num_list, K):
    if case[0] == '0':             # 앞 자리가 0인 경우 배제
        continue
    

    target = int(''.join(case))
    original_target = target
    while target%M==0 :
        target = target//M
    if target in mul and original_target in add :
        count+=1

print(count)