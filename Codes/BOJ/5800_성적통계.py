import sys

input = sys.stdin.readline

k = int(input())
for class_num in range(1, k + 1):
    temp = list(map(int, input().split()))
    n, scores = temp[0], temp[1:]
    scores.sort()
    max_score = scores[-1]
    min_score = scores[0]
    largest_gap = 0
    for i, score in enumerate(scores):
        if i == len(scores) - 1:
            break
        largest_gap = max(largest_gap, scores[i + 1] - score)

    print(f"Class {class_num}")
    print(f"Max {max_score}, Min {min_score}, Largest gap {largest_gap}")
