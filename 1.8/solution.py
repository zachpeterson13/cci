def zero_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    rows_to_zero = [False] * num_rows
    cols_to_zero = [False] * num_cols

    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val != 0:
                continue

            rows_to_zero[i] = True
            cols_to_zero[j] = True

    for i, val in enumerate(rows_to_zero):
        if val is True:
            zero_row(i, matrix)

    for i, val in enumerate(cols_to_zero):
        if val is True:
            zero_col(i, matrix)


def zero_row(row_to_zero: int, matrix):
    for i, row in enumerate(matrix):
        if i == row_to_zero:
            for j, _ in enumerate(row):
                matrix[i][j] = 0


def zero_col(col_to_zero: int, matrix) -> None:
    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if j == col_to_zero:
                matrix[i][j] = 0


if __name__ == "__main__":
    matrix1 = [
        [0, 2, 3],
        [1, 3, 3],
        [1, 3, 0],
        [1, 3, 3],
        [1, 3, 0],
        [1, 3, 3],
    ]

    zero_matrix(matrix1)

    for row in matrix1:
        print(row)
