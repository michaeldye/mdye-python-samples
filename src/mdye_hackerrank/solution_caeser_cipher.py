"""."""

#!/bin/python3

import os

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
MIN_LOWER = 97
MIN_UPPER = 65


def caesarCipher(s: str, k: int) -> str:  # noqa: D103, N802
    enc = ""

    # Write your code here
    for ch in s:
        if ch.isalpha():
            # set starting charset index for ascii to either ascii uppercase
            # range start or ascii lowercase range start
            min_range = MIN_LOWER if ch.islower() else MIN_UPPER

            v = ord(ch)

            # how far into the beginning of the char range the desired char is
            offset = ((v + k) - min_range) % 26
            nv = min_range + offset
            ch = chr(nv)

        enc += ch

    return enc


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")  # noqa: SIM115

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
