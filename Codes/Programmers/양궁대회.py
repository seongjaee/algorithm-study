from itertools import combinations_with_replacement


def solution(n, info):
    combs = list(combinations_with_replacement(range(10, -1, -1), n))
    max_value = 0
    max_c = []
    for c in combs:
        apeach = 0
        ryan = 0
        ryan_info = [0] * 11
        for i in c:
            ryan_info[i] += 1

        for i in range(11):
            score = 10 - i
            if info[i] == 0 and ryan_info[i] == 0:
                continue
            if info[i] >= ryan_info[i]:
                apeach += score
            else:
                ryan += score

        if max_value < ryan - apeach:
            max_value = ryan - apeach
            max_c = ryan_info

    if max_value:
        return max_c
    else:
        return [-1]


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))


# 두번째 풀이
def cal_diff(ryan, apeach):
    ryan_score = 0
    apeach_score = 0
    for i in range(11):
        score = 10 - i
        if ryan[i] == apeach[i] == 0:
            continue
        if ryan[i] > apeach[i]:
            ryan_score += score
        else:
            apeach_score += score

    return ryan_score - apeach_score


def solution(n, info):
    max_diff = 0
    answer = [-1]

    def bruteforce(score, level):
        nonlocal max_diff, answer
        if level == n:
            diff = cal_diff(visited, info)
            if max_diff < diff:
                max_diff = diff
                answer = visited[:]
            return

        if score < 11:
            visited[10 - score] += 1
            bruteforce(score, level + 1)
            visited[10 - score] -= 1
            bruteforce(score + 1, level)

    visited = [0] * 11
    bruteforce(0, 0)

    return answer


# 세번째 풀이
def cal_diff(ryan_info, apeach_info):
    result = 0
    for i in range(10):
        if ryan_info[i] == apeach_info[i] == 0:
            continue
        elif ryan_info[i] > apeach_info[i]:
            result += 10 - i
        else:
            result -= 10 - i
    return result


def solution(n, info):
    ryan_info = [0] * 11
    max_diff = 0
    answer = [-1]

    def backtrack(level, arrow_cnt):
        nonlocal max_diff, answer
        if level == -1:
            diff = cal_diff(ryan_info, info)
            if max_diff < diff:
                max_diff = diff
                answer = ryan_info[:]
            return

        if arrow_cnt < n:
            ryan_info[level] += 1
            backtrack(level, arrow_cnt + 1)
            ryan_info[level] -= 1

        backtrack(level - 1, arrow_cnt)

    backtrack(10, 0)

    return answer
