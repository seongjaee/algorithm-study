from collections import deque
import sys

input = sys.stdin.readline

DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
START_DIR = [None, 1, 2]


def init_tagger_move_dist(n):
    result = []
    for i in range(1, n):
        result += [i, i]
    result += [n - 1]

    return deque(result + result[::-1])


def calc_distance_with_tagger(runner_x, runner_y):
    tx, ty, _, _ = tagger
    return abs(tx - runner_x) + abs(ty - runner_y)


def runner_move(runner_num):
    x, y, d = runners[runner_num]
    if calc_distance_with_tagger(x, y) > 3:
        return

    runner_matrix[x][y].remove(runner_num)
    nx, ny = x + DELTA[d][0], y + DELTA[d][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        d = runner_next_dir(d)
        nx, ny = x + DELTA[d][0], y + DELTA[d][1]

    if (nx, ny) == (tagger[0], tagger[1]):
        nx, ny = x, y

    runners[runner_num] = (nx, ny, d)
    runner_matrix[nx][ny].add(runner_num)


def runner_next_dir(now_d):
    return (now_d + 2) % 4


def tagger_turn():
    global remain_dist
    TAGGER_MOVE_DISTANCES.append(TAGGER_MOVE_DISTANCES.popleft())
    remain_dist = TAGGER_MOVE_DISTANCES[0]
    _, _, td, is_reverse = tagger
    tagger[2] = (td - 1) % 4 if is_reverse else (td + 1) % 4


def tagger_move():
    global tagger, remain_dist
    tx, ty, td, is_reverse = tagger
    dx, dy = DELTA[td]
    nx, ny = tx + dx, ty + dy
    remain_dist -= 1
    if remain_dist == 0:
        tagger_turn()

    if (nx, ny) == (0, 0):
        tagger[0] = 0
        tagger[1] = 0
        tagger[2] = 2
        tagger[3] = True
        return

    if (nx, ny) == (n // 2, n // 2):
        tagger[0] = n // 2
        tagger[1] = n // 2
        tagger[2] = 0
        tagger[3] = False
        return

    tagger[0] = nx
    tagger[1] = ny


def look_forward():
    tx, ty, td, _ = tagger
    sights = []
    dx, dy = DELTA[td]
    for i in range(3):
        nx, ny = tx + dx * i, ty + dy * i
        sights.append((nx, ny))

    result = []
    for x, y in sights:
        if x < 0 or x >= n or y < 0 or y >= n:
            break
        if tree_matrix[x][y]:
            continue
        if len(runner_matrix[x][y]) > 0:
            result += list(runner_matrix[x][y])

    return result


def catch(time, runner_nums):
    global score
    score += (time + 1) * len(runner_nums)
    for runner_num in runner_nums:
        rx, ry, _ = runners.pop(runner_num)
        runner_matrix[rx][ry] = set()


n, m, h, k = map(int, input().split())
tagger = [n // 2, n // 2, 0, False]  # x, y, dir, is_reverse
TAGGER_MOVE_DISTANCES = init_tagger_move_dist(n)
remain_dist = TAGGER_MOVE_DISTANCES[0]
score = 0

runners = {}
runner_matrix = [[set() for _ in range(n)] for _ in range(n)]
for i in range(m):
    x, y, d = map(int, input().split())
    runners[i] = (x - 1, y - 1, START_DIR[d])
    runner_matrix[x - 1][y - 1].add(i)

tree_matrix = [[False] * n for _ in range(n)]
for _ in range(h):
    tree_x, tree_y = map(int, input().split())
    tree_matrix[tree_x - 1][tree_y - 1] = True

for time in range(k):
    for runner_num in runners.keys():
        runner_move(runner_num)
    tagger_move()
    runner_nums = look_forward()
    catch(time, runner_nums)

print(score)
