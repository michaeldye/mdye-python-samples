"""."""

import os
import sys
from pathlib import Path

if __name__ == "__main__":
    # given
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    m = {}

    for num in a:
        if num in m:
            m[num] += 1
        else:
            m[num] = 1

    result = None
    for num, ct in m.items():
        if ct == 1:
            result = num

    if not result:
        sys.exit(4)

    with Path(os.environ["OUTPUT_PATH"]).open("w", encoding="utf-8") as outf:
        outf.write(f"{result}\n")

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
