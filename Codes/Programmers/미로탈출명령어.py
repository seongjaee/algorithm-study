"""
순서 : d, l, r, u
"""


def get_min_dist(x, y, r, c):
    return abs(x - r) + abs(y - c)


def solution(n, m, x, y, r, c, k):
    answer = ""
    min_dist = get_min_dist(x, y, r, c)

    if min_dist > k or (min_dist - k) % 2 != 0:
        return "impossible"

    while get_min_dist(x, y, r, c) < k:
        if x < n:
            answer += "d"
            x += 1
        elif y > 1:
            answer += "l"
            y -= 1
        elif y < m:
            answer += "r"
            y += 1
        else:
            answer += "u"
            x -= 1
        k -= 1

    print(answer, x, y, r, c)

    while (x, y) != (r, c):
        if x < r and x < n:
            answer += "d"
            x += 1
        elif y > c and y > 1:
            answer += "l"
            y -= 1
        elif y < c and y < m:
            answer += "r"
            y += 1
        else:
            answer += "u"
            x -= 1

    return answer


print(solution(3, 4, 2, 3, 3, 1, 5))
