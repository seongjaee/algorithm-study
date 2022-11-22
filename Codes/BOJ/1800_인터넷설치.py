from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = 1e7


# 가중치가 value 이상인 간선을 k개 이하로 거쳐서 n을 갈 수 있나요
def check(value):
    heap = [(0, 1)]
    cnts = [k + 2] * (n + 1)
    cnts[1] = 0
    while heap:
        cnt, node = heappop(heap)
        if cnts[node] < cnt:
            continue

        for nxt_node, nxt_cost in graph[node]:
            nxt_cnt = cnt + 1 if nxt_cost > value else cnt
            if nxt_cnt > k:
                continue
            if nxt_node == n:
                return True
            if cnts[nxt_node] <= nxt_cnt:
                continue

            cnts[nxt_node] = nxt_cnt
            heappush(heap, (nxt_cnt, nxt_node))

    return False


n, p, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

answer = -1
left, right = -1, 1000001
while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
        answer = mid
    else:
        left = mid

print(answer)
