from heapq import heappush, heappop


def solution(n, k, enemy):
    answer = 0
    k_max = []
    k_max_sum = 0
    total = 0
    for idx, num in enumerate(enemy):
        heappush(k_max, num)
        k_max_sum += num
        total += num

        if len(k_max) > k:
            temp = heappop(k_max)
            k_max_sum -= temp

        if total - k_max_sum > n:
            return idx

    return len(enemy)
