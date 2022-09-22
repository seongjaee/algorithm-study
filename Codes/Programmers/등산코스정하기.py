from heapq import heappop, heappush

INF = 1e10


def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    graph = [[] for _ in range(1 + n)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    answer_intensity = INF
    answer_summit = n

    intensities = [INF] * (n + 1)
    heap = []
    for gate in gates:
        heappush(heap, (0, gate))
        intensities[gate] = 0

    while heap:
        dist, node = heappop(heap)

        if intensities[node] < dist:
            continue

        for nxt_node, nxt_cost in graph[node]:
            nxt_intensity = max(dist, nxt_cost)
            if answer_intensity < nxt_intensity:
                continue
            if intensities[nxt_node] <= nxt_intensity:
                continue
            intensities[nxt_node] = nxt_intensity

            if nxt_node in summits:
                if answer_intensity == nxt_intensity:
                    answer_summit = min(answer_summit, nxt_node)
                else:
                    answer_intensity = nxt_intensity
                    answer_summit = nxt_node
                continue

            heappush(heap, (nxt_intensity, nxt_node))

    return [answer_summit, answer_intensity]
