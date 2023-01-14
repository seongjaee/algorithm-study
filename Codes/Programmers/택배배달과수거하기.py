def solution(cap, n, deliveries, pickups):
    answer = 0

    di = n - 1
    pi = n - 1
    while di >= 0 or pi >= 0:
        for i in range(di, -1, -1):
            if deliveries[i] > 0:
                di = i
                break
        else:
            di = -1

        for i in range(pi, -1, -1):
            if pickups[i] > 0:
                pi = i
                break
        else:
            pi = -1

        answer += 2 * (max(di, pi) + 1)
        d_cnt = cap
        p_cnt = cap
        while d_cnt > 0 and di >= 0:
            if deliveries[di] >= d_cnt:
                deliveries[di] -= d_cnt
                d_cnt = 0
            else:
                d_cnt -= deliveries[di]
                deliveries[di] = 0
                di -= 1

        while p_cnt > 0 and pi >= 0:
            if pickups[pi] >= p_cnt:
                pickups[pi] -= p_cnt
                p_cnt = 0
            else:
                p_cnt -= pickups[pi]
                pickups[pi] = 0
                pi -= 1

    return answer


cap = 2
n = 2
deliveries = [0, 6]
pickups = [0, 0]


print(solution(cap, n, deliveries, pickups))
