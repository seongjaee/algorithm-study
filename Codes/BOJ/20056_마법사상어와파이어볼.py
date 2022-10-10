import sys

input = sys.stdin.readline


def simulate():
    global fireballs_with_pos
    fireballs_on_same_pos = {}  # (i, j) : [(m, s, d)]

    for i, j, m, s, d in fireballs_with_pos:
        di, dj = DELTA[d]
        ni, nj = (i + s * di) % N, (j + s * dj) % N
        fireballs_on_same_pos[(ni, nj)] = fireballs_on_same_pos.get((ni, nj), []) + [
            (m, s, d)
        ]

    fireballs_with_pos = []
    for (i, j), fireballs in fireballs_on_same_pos.items():
        if len(fireballs) == 1:
            fireballs_with_pos.append((i, j, *fireballs[0]))
            continue

        nxt_mass = int(sum([m for m, _, _ in fireballs]) / 5)
        if nxt_mass == 0:
            continue
        nxt_speed = int(sum([s for _, s, _ in fireballs]) / len(fireballs))
        is_all_odd_or_even = len({d % 2 for _, _, d in fireballs}) == 1
        nxt_ds = [0, 2, 4, 6] if is_all_odd_or_even else [1, 3, 5, 7]

        for nxt_d in nxt_ds:
            fireballs_with_pos.append((i, j, nxt_mass, nxt_speed, nxt_d))


DELTA = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

N, M, K = map(int, input().split())

fireballs_with_pos = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs_with_pos.append((r - 1, c - 1, m, s, d))

for _ in range(K):
    simulate()

answer = sum([m for _, _, m, _, _ in fireballs_with_pos])
print(answer)
