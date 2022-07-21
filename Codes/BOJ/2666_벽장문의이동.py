from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = 1e10


def bfs(left, right):
    move_cnt = 0
    used_cnt = 0
    i = 0
    while i < n and (left == numbers[i] or right == numbers[i]):
        used_cnt += 1
        i += 1

    queue = [(used_cnt, move_cnt, left, right, i)]

    while queue:
        used_cnt, move_cnt, left, right, i = heappop(queue)
        if used_cnt == m:
            return move_cnt

        nxt = numbers[i]
        if nxt < left:
            heappush(queue, (used_cnt + 1, move_cnt + left - nxt, nxt, right, i + 1))

        elif nxt > right:
            heappush(queue, (used_cnt + 1, move_cnt + nxt - right, left, nxt, i + 1))

        else:
            heappush(queue, (used_cnt + 1, move_cnt + nxt - left, nxt, right, i + 1))
            heappush(queue, (used_cnt + 1, move_cnt + right - nxt, left, nxt, i + 1))


n = int(input())
left, right = map(int, input().split())
left -= 1
right -= 1
left, right = min(left, right), max(left, right)
m = int(input())
numbers = [int(input()) - 1 for _ in range(m)]

print(bfs(left, right))
