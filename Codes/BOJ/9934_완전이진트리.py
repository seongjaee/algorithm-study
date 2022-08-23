def solution(arr, level):
    m = len(arr)
    result[level].append(arr[m // 2])
    if m != 1:
        solution(arr[: m // 2], level + 1)
        solution(arr[m // 2 + 1 :], level + 1)


k = int(input())
numbers = list(map(int, input().split()))

result = [[] for _ in range(k)]
solution(numbers, 0)
for row in result:
    print(*row)
