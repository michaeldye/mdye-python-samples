"""."""

import os
import sys


def _diagonal_difference(arr: list[list[int]]) -> int:
    def coords_to_vals(locs: list[tuple[int, int]]) -> list[int]:
        res = []
        for x, y in locs:
            res.append(arr[x][y])
        return res


    l_coords = []
    for v in range(len(arr)):
        l_coords.append((v,v))

    r_coords = []
    for ix in range(len(arr)):
        x = ix
        y = len(arr) - ix - 1
        r_coords.append((x,y))

    print(f"{l_coords=}, {r_coords=}", file=sys.stderr)

    return abs(sum(coords_to_vals(l_coords)) - sum(coords_to_vals(r_coords)))


if __name__ == "__main__":
    # given
    fptr = open(os.environ["OUTPUT_PATH"], "w")  # noqa: SIM115

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = _diagonal_difference(arr)
    fptr.write(str(result) + "\n")
    fptr.close()


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
