from heapq import heappop, heappush

INF = 1e4


def solution(alp, cop, problems):
    apl_goal = 0
    cop_goal = 0
    for alp_req, cop_req, _, _, _ in problems:
        apl_goal = max(apl_goal, alp_req)
        cop_goal = max(cop_goal, cop_req)

    distances = [[INF] * 151 for _ in range(151)]
    distances[alp][cop] = 0
    heap = [(0, alp, cop)]

    while heap:
        time, alp, cop = heappop(heap)

        if (alp, cop) == (apl_goal, cop_goal):
            return time

        if alp < apl_goal and distances[alp + 1][cop] > time + 1:
            distances[alp + 1][cop] = time + 1
            heappush(heap, (time + 1, alp + 1, cop))

        if cop < cop_goal and distances[alp][cop + 1] > time + 1:
            distances[alp][cop + 1] = time + 1
            heappush(heap, (time + 1, alp, cop + 1))

        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req <= alp and cop_req <= cop:
                nxt_alp = min(alp + alp_rwd, apl_goal)
                nxt_cop = min(cop + cop_rwd, cop_goal)

                if distances[nxt_alp][nxt_cop] > time + cost:
                    distances[nxt_alp][nxt_cop] = time + cost
                    heappush(heap, (time + cost, nxt_alp, nxt_cop))

    return 0
