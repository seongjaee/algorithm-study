def solution(k, m, score):
    answer = 0
    score.sort()
    while len(score) >= m:
        min_value = k
        for _ in range(m):
            min_value = min(min_value, score.pop())
        answer += min_value * m

    return answer
