from copy import deepcopy


def solution(info, edges):
    answer = 0

    def backtrack(now, candidates, visited, sheep, wolf):
        nonlocal answer
        answer = max(answer, sheep)

        nxt_candidates = deepcopy(candidates)

        nxt_candidates.remove(now)
        for nxt in graph[now]:
            nxt_candidates.add(nxt)

        for nxt in nxt_candidates:
            if visited & (1 << nxt):
                continue
            nxt_sheep = sheep + (info[nxt] + 1) % 2
            nxt_wolf = wolf + info[nxt]
            if nxt_wolf >= nxt_sheep:
                continue
            backtrack(nxt, nxt_candidates, visited | (1 << nxt), nxt_sheep, nxt_wolf)

    n = len(info)
    graph = [[] for _ in range(n)]

    for a, b in edges:
        graph[a].append(b)

    backtrack(0, {0}, 1, 1, 0)

    return answer


# 두번째 풀이
def solution(info, edges):
    def backtrack(sheep, wolf):
        nonlocal answer
        if sheep <= wolf:
            return
        answer = max(answer, sheep)

        for i in range(n):
            if not adjacency[i] or visited[i]:
                continue

            visited[i] = True
            adjacency[i] = False
            for nxt in graph[i]:
                adjacency[nxt] = True

            backtrack(sheep + int(info[i] == 0), wolf + int(info[i] == 1))

            visited[i] = False
            adjacency[i] = True
            for nxt in graph[i]:
                adjacency[nxt] = False

    n = len(info)
    graph = [[] for _ in range(n)]
    for p, c in edges:
        graph[p].append(c)

    visited = [False] * n
    adjacency = [False] * n

    visited[0] = True
    for nxt in graph[0]:
        adjacency[nxt] = True

    answer = 0
    backtrack(1, 0)

    return answer
