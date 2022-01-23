from itertools import combinations, permutations


N,K = map(int,input().split())
mmax = [0,9,99,999,9999,99999]
sol1 = set()
for_sol2 = ['0','1','2','3','4','5','6','7','8','9']
sol2 = []
sol22222 = []
fsol2 = []
plz = set()
count = 0
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출2
    return [i for i in range(2, n) if sieve[i] == True]

prime = prime_list(mmax[N])
print(prime)
for i in range(len(prime)-1) :
    for j in range(i+1, len(prime)) :
        if prime[i]+prime[j] <= mmax[N] :
            sol1.add(prime[i]+prime[j])
print(sol1)       
if N==1 :
    sol2 = [1,2,3,4,5,6,7,8,9]
elif N==2:
    sol22222 = list(permutations(for_sol2,N))
    for a,b in sol22222 :
        if a == '0' :
            continue
        else :
            sol2.append(int(a+b))
elif N==3:
    sol22222 = list(permutations(for_sol2,N))
    for a,b,c in sol22222 :
        if a == '0' :
            continue
        else :
            sol2.append(int(a+b+c))

elif N==4:
    sol22222 = list(permutations(for_sol2,N))
    for a,b,c,d in sol22222 :
        if a == '0' :
            continue
        else :
            sol2.append(int(a+b+c+d))
            
elif N==5:
    sol22222 = list(permutations(for_sol2,N))
    for a,b,c,d,e in sol22222 :
        if a == '0' :
            continue
        else :
            sol2.append(int(a+b+c+d+e))

    
for i in range(len(prime)) :
    for j in range(len(prime)) :
        if prime[i]*prime[j] <= mmax[N] :
            plz.add(prime[i]*prime[j])
print(plz)

for i in range(len(sol2)):
    n=sol2[i]
    if n in sol1:
        while n%K==0 :
            n //= K
        if n in plz :
            print(sol2[i])
            count +=1

print(count)
    
