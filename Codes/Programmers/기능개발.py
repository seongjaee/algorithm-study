from math import ceil


def solution(progresses, speeds):
    answer = []
    remain = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    now = 0
    for time in remain:
        if time > now:
            answer.append(1)
            now = time
        else:
            answer[-1] += 1

    return answer
