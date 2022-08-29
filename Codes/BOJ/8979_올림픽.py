import sys

input = sys.stdin.readline


def solution(info):
    result = 1
    now_score = (1e8, 1e8, 1e8)
    for idx, (num, g, s, b) in enumerate(info):
        if (g, s, b) < now_score:
            result = idx + 1
            now_score = (g, s, b)
        if num == k:
            return result


n, k = map(int, input().split())

info = [tuple(map(int, input().split())) for _ in range(n)]
info.sort(key=lambda arr: (-arr[1], -arr[2], -arr[3]))

print(solution(info))
