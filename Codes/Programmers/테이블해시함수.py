def solution(data, col, row_begin, row_end):
    col -= 1
    row_begin -= 1
    row_end -= 1
    data.sort(key=lambda tup: (tup[col], -tup[0]))

    S = [sum([value % (idx + 1) for value in tup]) for idx, tup in enumerate(data)]
    answer = 0
    for i in range(row_begin, row_end + 1):
        answer ^= S[i]

    return answer
