import sys

input = sys.stdin.readline


def sort_key(row):
    return (-int(row[1]), int(row[2]), -int(row[3]), row[0])


n = int(input())
scores = [input().split() for _ in range(n)]
scores.sort(key=sort_key)
for score in scores:
    print(score[0])
