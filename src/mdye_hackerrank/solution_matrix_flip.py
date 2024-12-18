"""."""

import os

#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


# sample input:
# [x] n = 1
# [] n = 2


def flippingMatrix(matrix: list[list[int]]) -> int:  # noqa: D103, N802
    n = len(matrix) // 2

    # it's a quadrant so we only need to find the 4 possible values for each place in the submatrix, sum those and keep the max

    max_sum = 0
    for rx in range(n):  # 0
        last_rx = len(matrix) - rx - 1  # 3

        for cx in range(n):  # 1
            last_cx = len(matrix) - cx - 1  # 2

            a = matrix[rx][cx]  # me!
            b = matrix[last_rx][cx]  # same column, last row's item
            c = matrix[rx][last_cx]  # same row, last column's item
            d = matrix[last_rx][last_cx]  # last row, last column

            max_sum += max(a, b, c, d)

    return max_sum


if __name__ == "__main__":
    with open(os.environ["OUTPUT_PATH"], "w") as fptr:
        q = int(input().strip())

        for _ in range(q):
            n = int(input().strip())

            matrix = []

            for _ in range(2 * n):
                matrix.append(list(map(int, input().rstrip().split())))

            result = flippingMatrix(matrix)

            fptr.write(str(result) + "\n")

        fptr.close()


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
