N, K = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x: (-int(x[1]), -int(x[2]), -int(x[3])))

prev_gold , prev_silver , prev_bronze , rank,equal = 0,0,0,0,1

for line in data :
    target, gold, silver, bronze = map(int, line)
    if gold == prev_gold and silver == prev_silver and bronze == prev_bronze:
        equal += 1
    else:
        prev_gold, prev_silver, prev_bronze, rank = gold, silver, bronze, rank + equal
        equal = 1

    if target == K:
        print(rank)
        break
