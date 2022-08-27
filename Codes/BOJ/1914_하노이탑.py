def solution(n, start, end, mid):
    if n == 0:
        return
    solution(n - 1, start, mid, end)
    print(start, end)
    solution(n - 1, mid, end, start)


n = int(input())
print(2**n - 1)
if n <= 20:
    solution(n, 1, 3, 2)
