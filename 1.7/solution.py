def rotate_matrix(m):
    n = len(m)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # top
            temp = m[first][i]

            # left -> top
            m[first][i] = m[last - offset][first]

            # bot -> left
            m[last - offset][first] = m[last][last - offset]

            # right -> bot
            m[last][last - offset] = m[i][last]

            # top -> right
            m[i][last] = temp


if __name__ == "__main__":
    tests = [
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
            [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]],
        )
    ]

    import copy

    for input, expected in tests:
        actual = copy.deepcopy(input)
        rotate_matrix(actual)
        result = "PASSED" if actual == expected else "FAILED"

        print(f"{result}: {input} -> {actual}, {expected=}")
