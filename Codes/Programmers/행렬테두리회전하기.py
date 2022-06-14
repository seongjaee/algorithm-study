def solution(rows, cols, queries):
    def turn(query):
        r1, c1, r2, c2 = [x - 1 for x in query]
        temp = matrix[r1][c1]
        result = temp

        for i in range(r1, r2):
            matrix[i][c1] = matrix[i + 1][c1]
            result = min(result, matrix[i][c1])

        for j in range(c1, c2):
            matrix[r2][j] = matrix[r2][j + 1]
            result = min(result, matrix[r2][j])

        for i in range(r2, r1, -1):
            matrix[i][c2] = matrix[i - 1][c2]
            result = min(result, matrix[i][c2])

        for j in range(c2, c1, -1):
            matrix[r1][j] = matrix[r1][j - 1]
            result = min(result, matrix[r1][j])

        matrix[r1][c1 + 1] = temp
        answer.append(result)

    matrix = [[(cols * j) + i for i in range(1, cols + 1)] for j in range(rows)]
    answer = []

    for query in queries:
        turn(query)

    return answer
