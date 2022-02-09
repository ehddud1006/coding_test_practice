from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)

n = int(stdin.readline())
arr = []
res = [int(1e9)]
visited = set()
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))


def solve(cnt, cost, v):
    if cnt == 3:
        res[0] = min(res[0], cost)

    else:
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                temp_visit = set()
                temp_visit.add((i, j))
                tf = 1
                temp = arr[i][j]
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if -1 < nx < n and -1 < ny < n:
                        if (nx, ny) not in v:
                            temp += arr[nx][ny]
                            temp_visit.add((nx, ny))
                        else:
                            tf = 0
                            break
                    else:
                        tf = 0
                        break

                if tf and temp_visit:
                    v.update(temp_visit)
                    solve(cnt + 1, cost + temp, v)
                    v -= temp_visit


solve(0, 0, visited)
print(res[0])