# Sol 2 : 다익스트라 알고리즘 사용 횟수 <= (N + 1)
# 시간 소모 : 580ms

# 양방향 그래프가 경사 트리의 구조일 경우 == (1 + 1)
# 양방향 그래프가 루트 노드와 리프 노드로만 구성된 경우 == (N + 1)
# (이 문제가 해당됨) 단방향 그래프일 경우 <= (N + 1)

import sys
import heapq


input = sys.stdin.readline
DEFAULT = -1


def solution() -> int:
    dijkstra_come(x)
    calc_list = [(come_costs[node], node) for node in range(1, n + 1)]
    calc_list.sort(reverse=True)                # '각 노드 -> x'를 계산할 노드들을 'x -> 해당 노드'의 최단 거리가 높은 순서대로 정렬
    for idx, val in enumerate(calc_list):       # 'x에서 돌아오는 최단 거리가 길수록 x로 가는 최단 경로 상에 경유하는 지점이 많다'의 경향성이 높을수록 효율적인 방식
        start_node = val[1]                     # 그러나 별로 의미 없는 것으로 판단됨.
        if go_costs[start_node] != DEFAULT:     # 이미 최단 거리를 구한 노드이면 건너뜀
            continue
        dijkstra_go(start_node, x)              # [start->node 1->node 2->...->node k->end]일 때 start, node 1, node 2, ..., node k 각각에서 end까지의 최단 거리를 구하는 함수

    best_cost = 0
    for node in range(1, n + 1):
        current_cost = go_costs[node] + come_costs[node]
        best_cost = max(best_cost, current_cost)

    return best_cost


def dijkstra_go(start: int, end: int):
    min_heap = [(0, start, start)]
    costs = [0] * (n + 1)               # 함수의 로컬 변수 costs: 'start -> node'의 최단 거리를 담은 리스트
    recents = [0] * (n + 1)             # 함수의 로컬 변수 recents: 'start -> node'까지의 최단 경로 상에서 node 도착 직전에 경유한 노드를 담은 리스트
    is_visited = [False] * (n + 1)
    while len(min_heap):
        cost, recent, current = heapq.heappop(min_heap)

        if is_visited[current]:
            continue

        costs[current] = cost
        recents[current] = recent
        is_visited[current] = True
        if current == end:
            go_costs[start] = cost
            break

        for idx, val in enumerate(connected[current]):
            heapq.heappush(min_heap, (cost + val[0], current, val[1]))
    
    recent = recents[end]                                       # start->end의 최단 경로 [start->node 1->node 2->...->node k->end]에서
    while recent != start:                                      # node k, node k-1, ..., node 1 순으로 go_costs를 계산함
        if go_costs[recent] == DEFAULT:
            go_costs[recent] = go_costs[end] - costs[recent]    # go_costs[recent]: recent에서 x까지의 최단 거리
        recent = recents[recent]


def dijkstra_come(start: int):
    min_heap = [(0, start)]
    while len(min_heap):
        cost, current = heapq.heappop(min_heap)
        if come_costs[current] != DEFAULT:
            continue

        come_costs[current] = cost

        for idx, val in enumerate(connected[current]):
            heapq.heappush(min_heap, (cost + val[0], val[1]))


if __name__ == '__main__':
    n, m, x = map(int, input().split())
    connected = [[] for node in range(n + 1)]
    for edge in range(m):
        depart, arrive, t = map(int, input().split())
        connected[depart].append((t, arrive))
    go_costs = [DEFAULT] * (n + 1)                  # go_costs[node]: 'node->x'의 최단 거리
    come_costs = [DEFAULT] * (n + 1)                # come_costs[node]: 'x->node'의 최단 거리
    sol = solution()
    print(sol)