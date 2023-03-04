def solution(sequence):
    seq1 = [num * ((idx % 2) * 2 - 1) for idx, num in enumerate(sequence)]
    seq2 = [num * (((idx + 1) % 2) * 2 - 1) for idx, num in enumerate(sequence)]
    dp1 = [seq1[0]]
    for i in range(1, len(seq1)):
        now = max(0, dp1[i - 1]) + seq1[i]
        dp1.append(now)

    dp2 = [seq2[0]]
    for i in range(1, len(seq2)):
        now = max(0, dp2[i - 1]) + seq2[i]
        dp2.append(now)

    return max(max(dp1), max(dp2))
