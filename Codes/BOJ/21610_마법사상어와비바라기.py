import sys

input = sys.stdin.readline

DELTA = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def move_clouds(d, s):
    d -= 1
    dy, dx = DELTA[d][0] * s, DELTA[d][1] * s
    for idx, cloud in enumerate(clouds):
        clouds[idx] = (cloud[0] + dy) % n, (cloud[1] + dx) % n


def rain():
    for y, x in clouds:
        matrix[y][x] += 1


def copy_water_bug():
    for y, x in clouds:
        cnt = 0
        for ny, nx in [(y - 1, x - 1), (y - 1, x + 1), (y + 1, x - 1), (y + 1, x + 1)]:
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if matrix[ny][nx] > 0:
                cnt += 1
        matrix[y][x] += cnt


def create_clouds():
    global clouds
    prev_clouds = set(clouds)
    next_clouds = []
    for y in range(n):
        for x in range(n):
            if matrix[y][x] >= 2 and (y, x) not in prev_clouds:
                next_clouds.append((y, x))
                matrix[y][x] -= 2

    clouds = next_clouds


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]

for _ in range(m):
    d, s = map(int, input().split())
    move_clouds(d, s)
    rain()
    copy_water_bug()
    create_clouds()

answer = 0
for row in matrix:
    for num in row:
        answer += num

print(answer)
