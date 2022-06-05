import sys
input = sys.stdin.readline

def solution(y, x, size):
    global cnt
    if y <= r < y + size and x <= c < x + size:
        if (y, x) == (r, c):
            print(cnt)
            return

        solution(y, x, size // 2)
        solution(y, x + size // 2, size // 2)
        solution(y + size // 2, x, size // 2)
        solution(y + size // 2, x + size // 2, size // 2)
    else:
        cnt += size * size

n, r, c = map(int, input().split())
N = 2 ** n
cnt = 0
solution(0, 0, N)
