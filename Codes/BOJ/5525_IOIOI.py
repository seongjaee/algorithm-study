n = int(input())
m = int(input())
s = input()

indices = []
for idx, io in enumerate(s):
    if io == "O" and 0 < idx < m - 1 and s[idx - 1] == s[idx + 1] == "I":
        indices.append(idx)

result = [1]
i = 1
while i < len(indices):
    if indices[i] - indices[i - 1] == 2:
        result[-1] += 1
    else:
        result.append(1)
    i += 1

answer = 0
for r in result:
    if r >= n:
        answer += r - n + 1

print(answer)
