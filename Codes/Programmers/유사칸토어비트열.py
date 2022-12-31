def solution(n, l, r):
    print(n, l, r)
    if n == 0:
        return 1

    # k번째 비트열의 i번째 값
    def get_bit(k, i):
        if k == 1:
            if i == 2:
                return 0
            return 1
        q, r = divmod(i, 5)
        prev_bit = get_bit(k - 1, q)
        if prev_bit == 0 or r == 2:
            return 0
        return 1

    prev_l, remainder_l = divmod(l - 1, 5)
    prev_r, remainder_r = divmod(r - 1, 5)

    answer = 4 * solution(n - 1, prev_l + 1, prev_r + 1)

    if get_bit(n - 1, prev_l):
        if remainder_l > 2:
            answer -= remainder_l - 1
        else:
            answer -= remainder_l

    if get_bit(n - 1, prev_r):
        if remainder_r > 1:
            answer -= 4 - remainder_r
        else:
            answer -= 3 - remainder_r

    return answer


print(solution(1, 1, 3))
