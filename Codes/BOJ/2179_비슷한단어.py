import sys

input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

max_prefix_length = 0

for i in range(n - 1):
    cur = words[i]
    for j in range(i + 1, n):
        nxt = words[j]
        for k in range(min(len(cur), len(nxt))):
            if cur[k] != nxt[k]:
                break
        else:
            k += 1

        if k > max_prefix_length:
            max_prefix_length = k
            answer = (cur, nxt)

print(answer[0])
print(answer[1])
