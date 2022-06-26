from heapq import heappop, heappush


def solution(food_times, k):
    n = len(food_times)
    heap = []
    for idx, time in enumerate(food_times):
        heappush(heap, (time, idx))

    remain = n
    remain_indices = [True] * n
    base = 0

    while heap:
        time, idx = heappop(heap)
        # 전부 빼도 남으면 전부 뺌
        if (k // remain) >= (time - base):
            k -= (time - base) * remain
            remain -= 1
            remain_indices[idx] = False
            base = time

        # 뺄 수 있는 만큼만 뺌
        else:
            k -= (k // remain) * remain
            base += k // remain
            break

    # 남은 k 빼기
    i = 0
    while k > 0 and i < n:
        if remain_indices[i] and food_times[i] > base:
            k -= 1
        i += 1

    # 가장 처음 나오는 먹을 수 있는 음식 출력
    for j in range(i, n):
        if remain_indices[j] and food_times[j] > base:
            return j + 1

    return -1
