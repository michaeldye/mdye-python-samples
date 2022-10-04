# -*- coding: utf-8 -*-


class Solution:
    def fromBinaryStr(self, s: str) -> int:
        # assumes big-endian

        v = 0

        for ix in range(len(s)):
            rx = len(s) - ix - 1
            v += int(s[rx]) * 2**ix

        return v

    def toBinaryStr(self, v: int) -> str:
        # will only work for v >= 0; is big-endian

        if v == 0:
            return "0"

        s = ""

        while v > 0:
            dig = ""
            if v % 2 == 1:
                dig = "1"
            else:
                dig = "0"

            # prepend digits b/c we processed lowest bit first
            s = dig + s

            v //= 2

        return s

    def addBinary(self, a: str, b: str) -> str:
        a_v = self.fromBinaryStr(a)
        b_v = self.fromBinaryStr(b)

        return self.toBinaryStr(a_v + b_v)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
