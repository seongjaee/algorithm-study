from itertools import permutations
from collections import deque


def clock(n, perm, weak):
    result = 10
    for _ in range(len(weak)):
        weak.append(weak.popleft() + n)
        new_weak = weak.copy()
        now = new_weak[0]
        i = 0
        while new_weak and i < len(perm):
            now += perm[i]
            while new_weak and new_weak[0] <= now:
                new_weak.popleft()
            if new_weak:
                now = new_weak[0]
            i += 1

        if new_weak:
            continue

        result = min(result, i)

    return result


def counter_clock(n, perm, weak):
    result = 10
    for _ in range(len(weak)):
        weak.append(weak.popleft() - n)
        new_weak = weak.copy()
        now = new_weak[0]
        i = 0
        while new_weak and i < len(perm):
            now -= perm[i]
            while new_weak and new_weak[0] >= now:
                new_weak.popleft()
            if new_weak:
                now = new_weak[0]
            i += 1

        if new_weak:
            continue

        result = min(result, i)

    return result


def solution(n, weak, dist):
    answer = 10
    perms = list(permutations(dist, len(dist)))
    reversed_weak = deque(weak[::-1])
    weak = deque(weak)

    for perm in perms:
        answer = min(answer, clock(n, perm, weak))
        answer = min(answer, counter_clock(n, perm, reversed_weak))

    if answer == 10:
        return -1

    return answer
