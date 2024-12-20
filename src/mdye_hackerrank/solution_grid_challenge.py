"""."""

import os
import sys


def gridChallenge(grid: list[str]) -> str:  # noqa: N802
    """."""
    exploded = []
    cols = 0

    # pretty inefficient, can we do better?
    for r in grid:
        if cols == 0:
            cols = len(r)  # set first
        elif cols != len(r):
            print(f"bogus input, cols val changed in row {r}", file=sys.stderr)
            raise RuntimeError("malformed input")
        exploded.append(sorted(r))

    if cols == 0:
        print("bug: cols not set")
        raise RuntimeError("bug")

    for cx in range(0, cols):
        coll = []
        for rx in range(0, len(exploded)):
            coll.append(exploded[rx][cx])
        if sorted(coll) != coll:
            return "NO"

    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")  # noqa: SIM115
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + "\n")

    fptr.close()
    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
