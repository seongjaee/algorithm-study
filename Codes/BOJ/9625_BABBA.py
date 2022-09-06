k = int(input())

result = [1, 0]
for _ in range(k):
    next = [0, 0]
    next[1] += result[0]
    next[0] += result[1]
    next[1] += result[1]
    result = next

print(*result)
