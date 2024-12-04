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

    turns = 1  # odd are player 1's turns, even are player 2's
    towers = [m] * n

    def move() -> bool:
        for ix, x in enumerate(towers):
            reduce_to = 0  # invalid value
            for y in reversed(range(1, x)):
                if x % y == 0:
                    # valid move; q: do we just pick the max we can?
                    reduce_to = y
            if reduce_to > 0:
                towers[ix] = reduce_to
                return False  # game not over
        return True  # we didn't return early, no move could be made, game is over

    while True:
        if move():
            break
        turns += 1

    # winner is opposite of player whose turn it is when the game ends
    return 1 if turns % 2 == 0 else 2


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
