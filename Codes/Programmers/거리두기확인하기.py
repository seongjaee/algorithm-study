from collections import deque

DELTA = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def is_anyone_nearby(place, visited, sy, sx):
    queue = deque([(sy, sx)])
    for _ in range(2):
        temp = deque()
        while queue:
            y, x = queue.popleft()
            visited[y][x] = True
            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= 5 or nx < 0 or nx >= 5:
                    continue
                if visited[ny][nx] or place[ny][nx] == "X":
                    continue
                temp.append((ny, nx))
                if place[ny][nx] == "P":
                    return True

        queue = temp


def check(place):
    visited = [[False] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":
                if is_anyone_nearby(place, visited, i, j):
                    return 0
    return 1


def solution(places):
    return [check(place) for place in places]
