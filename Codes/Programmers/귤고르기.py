def solution(k, tangerine):
    counter = {}
    for i in range(len(tangerine)):
        size = tangerine[i]
        counter[size] = counter.get(size, 0) + 1

    size_cnts = sorted(counter.items(), key=lambda tup: -tup[1])

    now = 0
    for idx, (size, cnt) in enumerate(size_cnts):
        now += cnt
        if now >= k:
            return idx + 1

    return len(size_cnts)
