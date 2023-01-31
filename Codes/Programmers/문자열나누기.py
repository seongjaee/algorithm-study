def solution(s):
    answer = 1
    now = s[0]
    cnt = 0
    for idx, char in enumerate(s[:-1]):
        cnt += 1 if char == now else -1
        if cnt == 0:
            answer += 1
            now = s[idx + 1]

    return answer
