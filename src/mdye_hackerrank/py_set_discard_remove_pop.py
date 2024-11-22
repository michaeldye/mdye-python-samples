"""."""

# problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true

# Noteworthy:
#
# getattr() is Python reflection builtin for members of an object (like
# functions by string name)
#

import sys

if __name__ == "__main__":
    n_ct = int(input())
    n = set(map(int, input().split()))
    assert len(n) == n_ct

    cmds = int(input())

    for cmdline in sys.stdin.readlines():
        d = cmdline.split()

        if len(d) == 1:
            assert d[0] == "pop"
            # do pop
            n.pop()
        else:
            assert len(d) == 2
            op = d[0]
            val = int(d[1])

            # do op
            op_fn = getattr(n, op)
            op_fn(val)

        # success, decrement
        cmds -= 1

    # ensure we've executed all
    assert cmds == 0
    print(sum(n))
