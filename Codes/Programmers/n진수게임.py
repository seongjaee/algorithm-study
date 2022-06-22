def convert(num, n):
    if num == 0:
        return "0"

    result = ""
    while num > 0:
        q, r = divmod(num, n)
        if r >= 10:
            result += chr(r + 55)
        else:
            result += str(r)
        num = q

    return result[::-1]


def solution(n, t, m, p):
    answer = ""
    num = 0
    order = 0
    p -= 1
    while len(answer) < t:
        for char in convert(num, n):
            if order == p:
                answer += char
            if len(answer) >= t:
                break
            order += 1
            order %= m
        num += 1

    return answer
