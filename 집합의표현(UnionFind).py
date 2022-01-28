
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

for i in range(e):
    op, a, b = map(int, input().split())
    if op == 0 :
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else :
            print('NO')
    
