def solution(n, stages):
    clear_users = [0] * (n + 1)
    trying_users = [0] * (n + 1)
    for stage in stages:
        for i in range(1, stage):
            clear_users[i] += 1
        if stage < n + 1:
            trying_users[stage] += 1

    fail_rates = [0] * (n + 1)
    for i in range(1, n + 1):
        if clear_users[i] + trying_users[i]:
            fail_rates[i] = trying_users[i] / (clear_users[i] + trying_users[i])

    result = sorted([i for i in range(1, n + 1)], key=lambda num: -fail_rates[num])
    return result


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
