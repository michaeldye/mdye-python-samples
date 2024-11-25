""".

problem: https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
"""

import os
import sys
from pathlib import Path


def _convert(twelve_h_time: str) -> str:
    td = twelve_h_time.split(":")
    h = int(td[0])
    m = int(td[1])
    s = int("".join(td[2][0:2]))

    ap = td[2][2]

    print(f"{h=}, {m=}, {s=}, {ap=}", file=sys.stderr)

    if ap == "A":
        if h == 12:
            h = 0
    elif h != 12:
        h += 12

    tv = (f"{v:02d}" for v in [h, m, s])
    return ":".join(tv)


if __name__ == "__main__":
    tt = input()

    outfile = Path(os.environ["OUTPUT_PATH"])
    assert outfile.parent.exists()

    with outfile.open(mode="w", encoding="utf-8") as outf:
        res = _convert(tt)
        outf.write(f"{res}\n")

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
