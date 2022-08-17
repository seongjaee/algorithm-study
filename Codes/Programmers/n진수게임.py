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





# 2번째 풀이
def convert(num, n):
    res = ''
    while num > 0:
        q, r = divmod(num, n)
        if r >= 10:
            res += chr(ord('A') + r - 10)
        else:
            res += str(r)
        num = q
    return res[::-1]

def solution(n, t, m, p):
    now_num = 0
    now_converted_num = '0'
    turn = 0
    answer = ''
    now_i = 0
    
    while len(answer) < t:
        if turn == p - 1:
            answer += now_converted_num[now_i]
        
        now_i += 1
        turn = (turn + 1) % m
        
        if now_i >= len(now_converted_num):
            now_num += 1
            now_converted_num = convert(now_num, n)
            now_i = 0

    return answer
