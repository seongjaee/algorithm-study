from collections import deque
from itertools import permutations
from copy import deepcopy

DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs(matrix, start, end):
    if start == end:
        return 0
    sy, sx = start
    ey, ex = end
    queue = deque([(sy, sx, 0)])
    visited = [[False] * 4 for _ in range(4)]
    visited[sy][sx] = True

    while queue:
        y, x, cnt = queue.popleft()
        nxt_points = set()
        for dy, dx in DELTA:
            for i in range(1, 4):
                ny, nx = i * dy + y, i * dx + x
                if ny > 3 or ny < 0 or nx > 3 or nx < 0:
                    break

                if i == 1:
                    nxt_points.add((ny, nx))

                # 더 이상 갈 수 없거나, 숫자가 있는 카드면 break
                if (
                    ny + dy > 3
                    or ny + dy < 0
                    or nx + dx > 3
                    or nx + dx < 0
                    or matrix[ny][nx]
                ):
                    nxt_points.add((ny, nx))
                    break

        for ny, nx in nxt_points:
            if visited[ny][nx]:
                continue
            if (ny, nx) == (ey, ex):
                return cnt + 1

            visited[ny][nx] = True
            queue.append((ny, nx, cnt + 1))

    return 0


def solution(board, r, c):
    answer = 1e10
    point = [[] for _ in range(7)]
    cards = set()

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                point[board[i][j]].append((i, j))
                cards.add(board[i][j])

    n = len(cards)
    perm = list(permutations(cards, n))  # 어떤 순서로 카드를 지울건지
    all_route = []  # 같은 카드 2개 중 어떤 걸 먼저 지울건지까지
    for p in perm:
        for i in range(1 << n):
            temp = []
            for j in range(n):
                if i & (1 << j):
                    temp.append((p[j], 1))
                else:
                    temp.append((p[j], 0))
            all_route.append(temp)

    for route in all_route:
        now = (r, c)
        result = 0
        new_board = deepcopy(board)
        for num, order in route:
            y1, x1 = point[num][order]
            y2, x2 = point[num][(order + 1) % 2]
            result += bfs(new_board, now, (y1, x1))
            result += bfs(new_board, (y1, x1), (y2, x2))
            if result >= answer:
                break

            new_board[y1][x1] = 0
            new_board[y2][x2] = 0
            now = (y2, x2)

        answer = min(answer, result)

    return answer + n * 2
