from heapq import heappop, heappush

INF = 1e10
DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(board):
    n = len(board)
    m = len(board[0])
    heap = [(0, 0, 0, -1)]
    distances = [[INF] * m for _ in range(n)]
    distances[0][0] = 0
    while heap:
        y, x, dist, d = heappop(heap)

        for nd in range(4):
            ny, nx = y + DELTA[nd][0], x + DELTA[nd][1]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if board[ny][nx] == 1:
                continue

            nxt_cost = 6 if (d != -1 and nd != d) else 1
            if nxt_cost + dist > distances[ny][nx]:
                continue
            distances[ny][nx] = nxt_cost + dist
            heappush(heap, (ny, nx, nxt_cost + dist, nd))

    return distances[-1][-1] * 100
