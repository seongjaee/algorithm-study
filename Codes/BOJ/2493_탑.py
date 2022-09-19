import sys

input = sys.stdin.readline

n = int(input())

towers = [*zip(range(n), map(int, input().split()))]

result = [0] * n
remain = []

while towers:
    cur_idx, cur_height = towers.pop()
    while remain:
        prev_idx, prev_height = remain[-1]
        if prev_height > cur_height:
            break
        result[prev_idx] = cur_idx + 1
        remain.pop()

    remain.append((cur_idx, cur_height))

print(*result)
