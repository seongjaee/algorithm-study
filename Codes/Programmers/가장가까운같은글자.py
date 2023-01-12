def solution(s):
    answer = []
    d = {}
    for idx, char in enumerate(s):
        if char in d:
            answer.append(idx - d[char])
        else:
            answer.append(-1)
        d[char] = idx

    return answer
