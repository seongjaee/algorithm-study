from collections import deque

DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def solution(board):
    n = len(board)

    def bfs():
        visited = [[[False, False] for _ in range(n)] for _ in range(n)]
        visited[0][0][0] = True
        queue = deque([(0, 0, 0, 0)])

        while queue:
            y1, x1, dr, cnt = queue.popleft()
            y2, x2 = y1 + DELTA[dr][0], x1 + DELTA[dr][1]
            if (y2, x2) == (n - 1, n - 1):
                return cnt

            # move
            for dy, dx in DELTA:
                ny1, nx1 = dy + y1, dx + x1
                ny2, nx2 = dy + y2, dx + x2
                if 0 <= ny1 < n and 0 <= ny2 < n and 0 <= nx1 < n and 0 <= nx2 < n:
                    if board[ny1][nx1] or board[ny2][nx2]:
                        continue
                    if visited[ny1][nx1][dr]:
                        continue

                    visited[ny1][nx1][dr] = True
                    queue.append((ny1, nx1, dr, cnt + 1))

            # rotate
            # (y1, x1) 기준
            # 세로
            if dr:
                # 반시계
                ny, nx = y1, x1 + 1
                ty, tx = y1 + 1, x1 + 1
                if (
                    nx < n
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[y1][x1][0]
                ):
                    visited[y1][x1][0] = True
                    queue.append((y1, x1, 0, cnt + 1))

                # 시계
                ny, nx = y1, x1 - 1
                ty, tx = y1 + 1, x1 - 1
                if (
                    nx >= 0
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[ny][nx][0]
                ):
                    visited[ny][nx][0] = True
                    queue.append((ny, nx, 0, cnt + 1))

            # 가로
            else:
                # 반시계
                ny, nx = y1 - 1, x1
                ty, tx = y1 - 1, x1 + 1
                if (
                    ny >= 0
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[ny][nx][1]
                ):
                    visited[ny][nx][1] = True
                    queue.append((ny, nx, 1, cnt + 1))

                # 시계
                ny, nx = y1 + 1, x1
                ty, tx = y1 + 1, x1 + 1
                if (
                    ny < n
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[y1][x1][1]
                ):
                    visited[y1][x1][1] = True
                    queue.append((y1, x1, 1, cnt + 1))

            # (y2, x2) 기준
            # 세로
            if dr:
                # 반시계
                ny, nx = y2, x2 - 1
                ty, tx = y2 - 1, x2 - 1
                if (
                    nx > 0
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[ny][nx][0]
                ):
                    visited[ny][nx][0] = True
                    queue.append((ny, nx, 0, cnt + 1))
                # 시계
                ny, nx = y2, x2 + 1
                ty, tx = y2 - 1, x2 + 1
                if (
                    nx < n
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[y2][x2][0]
                ):
                    visited[y2][x2][0] = True
                    queue.append((y2, x2, 0, cnt + 1))
            # 가로
            else:
                # 반시계
                ny, nx = y2 + 1, x2
                ty, tx = y2 + 1, x2 - 1
                if (
                    ny < n
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[y2][x2][1]
                ):
                    visited[y2][x2][1] = True
                    queue.append((y2, x2, 1, cnt + 1))
                # 시계
                ny, nx = y2 - 1, x2
                ty, tx = y2 - 1, x2 - 1
                if (
                    ny >= 0
                    and not board[ny][nx]
                    and not board[ty][tx]
                    and not visited[ny][nx][1]
                ):
                    visited[ny][nx][1] = True
                    queue.append((ny, nx, 1, cnt + 1))

    return bfs()
