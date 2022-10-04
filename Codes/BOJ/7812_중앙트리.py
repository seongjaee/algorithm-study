import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


def dfs(now, prev):
    node_cnts[now] = 1
    for nxt_node, nxt_cost in graph[now]:
        if nxt_node == prev:
            continue
        dfs(nxt_node, now)
        node_cnts[now] += node_cnts[nxt_node]
        sums[now] += nxt_cost * node_cnts[nxt_node] + sums[nxt_node]


def get_sum(now, prev, result):
    global answer
    answer = min(answer, result)

    for nxt_node, nxt_cost in graph[now]:
        if nxt_node == prev:
            continue

        # nxt_node를 루트로 했을 때 총 비용 합
        # = (now를 루트로 했을 때 총 비용 합) + now-nxt_node 비용 * now 방문 횟수
        get_sum(nxt_node, now, result + nxt_cost * (n - 2 * node_cnts[nxt_node]))


while True:
    n = int(input())
    if n == 0:
        break
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))

    # 루트 : 0
    sums = [0] * n  # 각 노드를 루트로 하는 서브 트리의 모든 정점까지 비용 합
    node_cnts = [0] * n  # 각 노드를 루트로 하는 서브 트리의 노드 개수 == 각 노드를 방문하는 횟수
    dfs(0, -1)

    answer = 1e10
    get_sum(0, -1, sums[0])

    print(answer)
