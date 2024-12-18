"""."""


#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

import os


def towerBreakers(n: int, m: int) -> int:  # noqa: D103, N802
    # Write your code here
    # ending condition: towers can't be reduced in height
    #
    # Reasons a given tower can't be reduced:
    # - There is no unit qty that evenly divides the current height of a tower
    # or
    # - The height is 1

    if m == 1 or n % 2 == 0:
        # second player wins b/c first player can't move *or* last tower will be
        # theirs to reduce to 1
        return 2
    # first player wins b/c last tower will be theirs to reduce to 1
    return 1


if __name__ == "__main__":
    with open(os.environ["OUTPUT_PATH"], "w") as fptr:
        t = int(input().strip())

        for _ in range(t):
            first_multiple_input = input().rstrip().split()
            n = int(first_multiple_input[0])
            m = int(first_multiple_input[1])
            result = towerBreakers(n, m)

            fptr.write(str(result) + "\n")

        fptr.close()

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
