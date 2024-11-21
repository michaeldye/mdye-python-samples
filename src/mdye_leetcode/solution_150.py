"""."""

import math
from typing import List


class Solution:
    def do_op(self, op_s: str, a: int, b: int) -> int:
        """."""
        if op_s == "+":
            ans = b + a
        elif op_s == "-":
            ans = b - a
        elif op_s == "/":
            ans = math.trunc(b / a)  # wut??
        elif op_s == "*":
            ans = b * a
        else:
            raise RuntimeError(f"Unknown op: {op_s}")

        return ans

    def eval_rpn(self, tokens: List[str]) -> int:
        """."""
        stack = []

        for t in tokens:
            # lame that python doesn't have a better way to test for negative
            # num than to conversion and catch exception
            try:
                stack.append(int(t))
            except ValueError:
                stack.append(self.do_op(t, stack.pop(), stack.pop()))

        # last value on stack is result of all operations
        return stack[-1]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
