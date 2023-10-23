import sys, decimal

decimal.getcontext().rounding = decimal.ROUND_HALF_UP
input = sys.stdin.readline


def solution():
    n = int(input())
    if n == 0:
        return 0

    counter = [0] * 31

    for _ in range(n):
        counter[int(input())] += 1

    offset = round(decimal.Decimal(n * 0.15), 0)
    temp = 0
    for i in range(1, 31):
        count = counter[i]
        temp += count
        counter[i] = 0
        if temp >= offset:
            counter[i] = temp - offset
            break

    temp = 0
    for i in range(30, 0, -1):
        count = counter[i]
        temp += count
        counter[i] = 0
        if temp >= offset:
            counter[i] = temp - offset
            break

    total_sum = 0
    total_count = 0
    for i, count in enumerate(counter):
        total_sum += i * count
        if count != 0:
            total_count += count

    return round(decimal.Decimal(total_sum) / decimal.Decimal(total_count), 0)


print(solution())
