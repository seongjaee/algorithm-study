def solution(n, numbers):
    s = sum(numbers)
    arr = [False] * (s + 1)

    for i in range(1 << n):
        temp = 0
        for j in range(n):
            if (1 << j) & i:
                temp += numbers[j]
        arr[temp] = True

    for i in range(1, s + 1):
        if not arr[i]:
            return i

    return s + 1


n = int(input())
numbers = list(map(int, input().split()))

print(solution(n, numbers))
