import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda arr: arr[0])
    answer = 1
    min_value = arr[0][1]
    for i in range(1, n):
        if min_value > arr[i][1]:
            answer += 1
            min_value = arr[i][1]

    print(answer)
