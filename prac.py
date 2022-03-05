n=3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
from collections import deque
def solution(n, computers):
    roots = [node for node in range(n)]

    def find_root(x: int) -> int:
        if roots[x] == x:
            return x
        
        roots[x] = find_root(roots[x])
        return roots[x]
    
    def union(a: int, b: int):
        root_a = find_root(a)
        root_b = find_root(b)
        
        if root_a > root_b:
            root_a, root_b = root_b, root_a
        
        roots[root_b] = root_a
        
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union(i, j)
    
    answer = len(set([find_root(node) for node in range(n)]))
    return answer

solution(n,computers)