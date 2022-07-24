from re import L
import sys

input = sys.stdin.readline

n = int(input())
people = set()
for _ in range(n):
    name, record = input().split()
    if record == "enter":
        people.add(name)
    else:
        if name in people:
            people.remove(name)

for name in sorted(list(people), reverse=True):
    print(name)
