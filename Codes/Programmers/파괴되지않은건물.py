def solution(board, skill):
    answer = 0
    n = len(board[0])
    m = len(board)

    presum = [[0] * (n + 1) for _ in range(m + 1)]
    for t, r1, c1, r2, c2, degree in skill:
        presum[r1][c1] += degree * (t * 2 - 3)
        presum[r1][c2 + 1] -= degree * (t * 2 - 3)

        presum[r2 + 1][c1] -= degree * (t * 2 - 3)
        presum[r2 + 1][c2 + 1] += degree * (t * 2 - 3)

    # 행 방향 누적합
    for i in range(m + 1):
        for j in range(1, n + 1):
            presum[i][j] += presum[i][j - 1]

    # 열 방향 누적합
    for i in range(1, m + 1):
        for j in range(n + 1):
            presum[i][j] += presum[i - 1][j]

    for i in range(m):
        for j in range(n):
            if presum[i][j] + board[i][j] > 0:
                answer += 1

    return answer
