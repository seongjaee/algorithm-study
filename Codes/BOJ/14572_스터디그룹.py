import sys

input = sys.stdin.readline


def calculate_efficency(left, right, group):
    student_count = right - left + 1
    temp = len(group)
    for value in group.values():
        if value >= student_count:
            temp -= 1
    return temp * student_count


STUDENT_NUM, ALGORITHM_NUM, MINIMUM_SCORE_DIFFERENCE = map(int, input().split())

scores_indices = []
known_algorithms = {}

for i in range(STUDENT_NUM):
    known_cnt, score = map(int, input().split())
    knowns = list(map(int, input().split()))
    scores_indices.append((score, i))
    known_algorithms[i] = knowns

scores_indices.sort(key=lambda x: x[0])

left, right = 0, 0
group = {}
max_efficency = 0

while right < STUDENT_NUM:
    if scores_indices[right][0] - scores_indices[left][0] <= MINIMUM_SCORE_DIFFERENCE:
        for algo in known_algorithms[scores_indices[right][1]]:
            group[algo] = group.get(algo, 0) + 1
        max_efficency = max(max_efficency, calculate_efficency(left, right, group))
        right += 1

    else:
        for algo in known_algorithms[scores_indices[left][1]]:
            if group[algo] == 1:
                group.pop(algo)
            else:
                group[algo] -= 1
        left += 1


print(max_efficency)
