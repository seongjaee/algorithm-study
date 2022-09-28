import sys

input = sys.stdin.readline

n = int(input())

name_birthday = []
for _ in range(n):
    name, dd, mm, yyyy = input().split()
    name_birthday.append((name, int(yyyy), int(mm), int(dd)))

name_birthday.sort(key=lambda tup: (tup[1], tup[2], tup[3]))
print(name_birthday[-1][0])
print(name_birthday[0][0])
