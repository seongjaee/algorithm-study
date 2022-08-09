import sys

input = sys.stdin.readline

# 팀 찾기
def link_team(hy, hx):
    stack = [(hy, hx)]
    mid = []

    while stack:
        y, x = stack.pop()
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if visited[ny][nx]:
                continue

            if matrix[ny][nx] == 2:
                visited[ny][nx] = True
                stack.append((ny, nx))
                mid.append((ny, nx))

            elif matrix[ny][nx] == 3:
                visited[ny][nx] = True
                tail = (ny, nx)

    return [(hy, hx)] + mid + [tail]


def reverse_team(team_idx):
    team = teams[team_idx]
    for y, x in team:
        matrix[y][x] = 4

    team = team[::-1]

    h, t = team[0], team[-1]
    matrix[h[0]][h[1]] = 1
    matrix[t[0]][t[1]] = 3
    for y, x in team[1:-1]:
        matrix[y][x] = 2

    teams[team_idx] = team


def move():
    new_teams = []
    # 한 번씩 회전
    for team in teams:
        hy, hx = team[0]
        for dy, dx in DELTA:
            ny, nx = hy + dy, hx + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if matrix[ny][nx] >= 3:  # 머리와 꼬리가 붙어있을 경우도 있음
                new_teams.append([(ny, nx)] + team[:-1])
                break

    # 행렬 초기화
    for team in teams:
        for y, x in team:
            matrix[y][x] = 4

    # 바뀐 팀대로 다시 색칠
    for team in new_teams:
        h, t = team[0], team[-1]
        matrix[h[0]][h[1]] = 1
        matrix[t[0]][t[1]] = 3
        for y, x in team[1:-1]:
            matrix[y][x] = 2

    return new_teams


def get_score(round):
    def score(y, x):
        for i, team in enumerate(teams):
            for j, point in enumerate(team):
                if point == (y, x):  # 사람을 만나는 경우
                    reverse_team(i)
                    return (j + 1) ** 2

    _, round = divmod(round, 4 * n)  # 라운드 4n == 라운드 0
    q, r = divmod(round, n)
    if q == 0:
        y = r
        for x in range(n):
            if 0 < matrix[y][x] < 4:
                return score(y, x)

    elif q == 1:
        x = r
        for y in range(n - 1, -1, -1):
            if 0 < matrix[y][x] < 4:
                return score(y, x)
    elif q == 2:
        y = n - 1 - r
        for x in range(n - 1, -1, -1):
            if 0 < matrix[y][x] < 4:
                return score(y, x)
    else:
        x = n - 1 - r
        for y in range(n):
            if 0 < matrix[y][x] < 4:
                return score(y, x)

    return 0


DELTA = [(-1, 0), (0, 1), (0, -1), (1, 0)]
n, m, k = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
total_score = 0
teams = []
visited = [[False] * n for _ in range(n)]

heads = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            teams.append(link_team(i, j))


for i in range(k):
    teams = move()
    total_score += get_score(i)

print(total_score)
