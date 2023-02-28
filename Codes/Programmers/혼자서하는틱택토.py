def count_row(board, mark):
    result = 0
    for row in board:
        if row == mark * 3:
            result += 1

    for i in range(3):
        if board[i][i] != mark:
            break
    else:
        result += 1

    for i in range(3):
        if board[i][2 - i] != mark:
            break
    else:
        result += 1

    board = ["".join(row) for row in zip(*board)]
    for row in board:
        if row == mark * 3:
            result += 1

    return result


def solution(board):
    O_count = 0
    X_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                O_count += 1
            elif board[i][j] == "X":
                X_count += 1

    if not (X_count <= O_count <= X_count + 1):
        return 0

    O_row_count = count_row(board, "O")
    X_row_count = count_row(board, "X")

    if O_row_count != 0 and X_row_count != 0:
        return 0

    if O_row_count != 0 and O_count == X_count:
        return 0

    if X_row_count != 0 and O_count > X_count:
        return 0

    return 1
