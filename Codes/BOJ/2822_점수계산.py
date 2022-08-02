import sys

input = sys.stdin.readline

scores = [(i + 1, int(input())) for i in range(8)]
scores.sort(key=lambda score: -score[1])

top5 = scores[:5]
total = sum([score[1] for score in top5])
indices = sorted([score[0] for score in top5])
print(total)
print(*indices)
