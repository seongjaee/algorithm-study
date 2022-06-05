import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [*map(int, input().split())]
B = [*map(int, input().split())]

print(*sorted(A + B))