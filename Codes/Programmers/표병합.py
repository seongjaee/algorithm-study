def solution(commands):
    answer = []
    matrix = [[None] * 50 for _ in range(50)]
    parents = [[(i, j) for j in range(50)] for i in range(50)]

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

        if (r1, c1) > (r2, c2):
            parents[r1][c1] = (r2, c2)
        else:
            parents[r2][c2] = (r1, c1)

    def pprint(r, c):
        pr, pc = find(r, c)
        print(pr, pc)
        return matrix[pr][pc]

    def merge(r1, c1, r2, c2):
        if matrix[r1][c1]:
            union((r1, c1), (r2, c2))
        elif matrix[r2][c2]:
            union((r2, c2), (r1, c1))
        else:
            union((r1, c1), (r2, c2))

    def unmerge(r, c):
        value = matrix[r][c]
        pr, pc = find(r, c)
        group = []
        for i in range(50):
            for j in range(50):
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
                for i in range(50):
                    for j in range(50):
                        if find(i, j) == (r, c):
                            matrix[i][j] = value
            else:
                value1, value2 = temp[1:]
                for i in range(50):
                    for j in range(50):
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


print(
    solution(
        [
            "UPDATE 1 1 menu",
            "UPDATE 1 2 category",
            "UPDATE 2 1 bibimbap",
            "UPDATE 2 2 korean",
            "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon",
            "UPDATE 3 2 korean",
            "UPDATE 3 3 noodle",
            "UPDATE 3 4 instant",
            "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian",
            "UPDATE 4 3 noodle",
            "MERGE 1 2 1 3",
            "MERGE 1 3 1 4",
            "UPDATE korean hansik",
            "UPDATE 1 3 group",
            "UNMERGE 1 4",
            "PRINT 1 3",
            "PRINT 1 4",
        ]
    )
)
