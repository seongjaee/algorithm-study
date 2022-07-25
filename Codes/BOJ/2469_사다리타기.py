import sys

input = sys.stdin.readline

k = int(input())
n = int(input())
final = list(input().rstrip())

matrix = [list(input().rstrip()) for _ in range(n)]
first = [chr(i + 65) for i in range(k)]

for row in matrix:
    if row[0] == "?":
        break
    for i, char in enumerate(row):
        if char == "-":
            first[i], first[i + 1] = first[i + 1], first[i]

for row in matrix[::-1]:
    if row[0] == "?":
        break
    for i, char in enumerate(row):
        if char == "-":
            final[i], final[i + 1] = final[i + 1], final[i]

answer = ""
for i in range(k - 1):
    if first[i] == final[i]:
        answer += "*"
        continue
    first[i], first[i + 1] = first[i + 1], first[i]
    if answer and answer[-1] == "-":
        break
    answer += "-"

if first == final:
    print(answer)
else:
    print("x" * (k - 1))
