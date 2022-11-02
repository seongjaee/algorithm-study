from bisect import bisect_left
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B.sort()

    answer = 0
    for a in A:
        i = bisect_left(B, a)
        answer += i

    print(answer)
