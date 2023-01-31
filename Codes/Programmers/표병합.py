def solution(commands):
    answer = []
    matrix = [[None] * 51 for _ in range(51)]
    parents = [[(i, j) for j in range(51)] for i in range(51)]

    def find(r, c):
        if parents[r][c] != (r, c):
            pr, pc = parents[r][c]
            return find(pr, pc)
        return parents[r][c]

    def union(point1, point2):
        r1, c1 = find(*point1)
        r2, c2 = find(*point2)
        if (r1, c1) == (r2, c2):
            return

        if matrix[r1][c1]:
            parents[r2][c2] = (r1, c1)
            matrix[r2][c2] = matrix[r1][c1]
        elif matrix[r2][c2]:
            parents[r1][c1] = (r2, c2)
            matrix[r1][c1] = matrix[r2][c2]
        else:
            parents[r2][c2] = (r1, c1)
            matrix[r2][c2] = matrix[r1][c1]

    def pprint(r, c):
        pr, pc = find(r, c)
        return matrix[pr][pc] if matrix[pr][pc] else "EMPTY"

    def merge(r1, c1, r2, c2):
        union((r1, c1), (r2, c2))

    def unmerge(r, c):
        value = matrix[r][c]
        pr, pc = find(r, c)
        group = []
        for i in range(1, 51):
            for j in range(1, 51):
                if find(i, j) == (pr, pc):
                    group.append((i, j))

        for i, j in group:
            matrix[i][j] = None
            parents[i][j] = (i, j)

        matrix[r][c] = value

    for cmd in commands:
        temp = cmd.split()
        if temp[0] == "UPDATE":
            if len(temp) == 4:
                r, c, value = temp[1:]
                r, c = int(r), int(c)
                r, c = find(r, c)
                for i in range(1, 51):
                    for j in range(1, 51):
                        if find(i, j) == (r, c):
                            matrix[i][j] = value
            else:
                value1, value2 = temp[1:]
                for i in range(1, 51):
                    for j in range(1, 51):
                        if matrix[i][j] == value1:
                            matrix[i][j] = value2

        elif temp[0] == "MERGE":
            r1, c1, r2, c2 = map(int, temp[1:])
            merge(r1, c1, r2, c2)

        elif temp[0] == "UNMERGE":
            r, c = map(int, temp[1:])
            unmerge(r, c)

        elif temp[0] == "PRINT":
            r, c = map(int, temp[1:])
            answer.append(pprint(r, c))

    return answer
