import sys

input = sys.stdin.readline


def process(atoms_with_pos):
    def get_next_point(i, j, speed, direction):
        di, dj = DELTA[direction]
        ni, nj = (i + di * speed) % N, (j + dj * speed) % N
        return ni, nj

    def get_new_mass(atoms_in_same_pos):
        return sum([m for m, _, _ in atoms_in_same_pos]) // 5

    def get_new_speed(atoms_in_same_pos):
        return sum([s for _, s, _ in atoms_in_same_pos]) // len(atoms_in_same_pos)

    def get_new_directions(atoms_in_same_pos):
        # 상하좌우, 대각선 둘 다 포함 => 대각선 반환
        if len(set([d % 2 for _, _, d in atoms_in_same_pos])) == 2:
            return [1, 3, 5, 7]
        else:
            return [0, 2, 4, 6]

    after_move = {}
    new_atoms_with_pos = []
    for atom in atoms_with_pos:
        i, j, m, s, d = atom
        ni, nj = get_next_point(i, j, s, d)
        after_move[(ni, nj)] = after_move.get((ni, nj), []) + [(m, s, d)]

    for point, atoms_in_same_pos in after_move.items():
        y, x = point
        # 노 합성
        if len(atoms_in_same_pos) == 1:
            m, s, d = atoms_in_same_pos[0]
            new_atoms_with_pos.append((y, x, m, s, d))
        # 합성이 일어남
        else:
            mass = get_new_mass(atoms_in_same_pos)
            if mass == 0:
                continue
            speed = get_new_speed(atoms_in_same_pos)
            directions = get_new_directions(atoms_in_same_pos)
            for d in directions:
                new_atoms_with_pos.append((y, x, mass, speed, d))

    return new_atoms_with_pos


DELTA = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
N, M, K = map(int, input().split())

atoms_with_pos = []
for _ in range(M):
    y, x, m, s, d = map(int, input().split())
    atoms_with_pos.append((y - 1, x - 1, m, s, d))

for _ in range(K):
    atoms_with_pos = process(atoms_with_pos)

answer = 0
for atom in atoms_with_pos:
    answer += atom[2]

print(answer)
