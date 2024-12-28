"""."""


def minimumBribes(q: list[int]) -> None:  # noqa: D103, N802
    bribes = 0

    # Solution from Nathan Abela. Algorithm: iterate from end -> head and
    # accumulate quantity of values from (max_promoted_position of curr) that
    # are > curr. So in case [1 2 5 3 7 8 6 4], we start with curr_val=4 and
    # count all values > 4 in q[1]-q[7] (0-indexed and inclusive), which is 4.
    # Then when curr_val=6, count all values > 6 in q[3]-q[6], which is 2.
    # Finally, when curr_val=3, the count of values > 3 in q[0]-q[2] is 1. So
    # the total quantity of accumulated bribes is 7.

    # It may be possible to process this from head -> end but how to determine
    # is not clear. The end -> head way lets us make a subset of values that is
    # just (max promoted) - (current position) and count just those promoted
    # beyond current.

    for ix in range(0, len(q)):
        curr_val = q[ix]

        natural_pos = curr_val - 1  # b/c zero-indexed natural pos

        max_promoted_pos = (
            natural_pos - 2
        )  # b/c curr could've been promoted up to 2 spaces ahead if they'd bribed

        if ix < max_promoted_pos:
            print("Too chaotic")
            return

        # protect from looking too far left when we get near end of iteration
        for jx in range(0 if max_promoted_pos < 0 else max_promoted_pos, ix):
            if q[jx] > curr_val:
                bribes += 1

    print(bribes)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
