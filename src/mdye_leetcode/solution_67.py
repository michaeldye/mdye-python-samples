"""."""


class Solution:
    # big-endian (most significant byte is at smallest memory address;
    # this is probably the most intuitive, but most hardware is little-endian

    def from_binary_str(self, s: str) -> int:
        """."""
        # assumes big-endian

        v = 0

        for ix in range(len(s)):
            # use ix (0...) for exponentiation, 2^0, 2^1, 2^2...
            # use rx (the reverse index) to iterate from least significant digit to most

            rx = len(s) - 1 - ix
            v += int(s[rx]) * 2**ix

        return v

    def to_binary_str(self, v: int) -> str:
        """."""
        # will only work for v >= 0; is big-endian

        if v == 0:
            return "0"

        s = ""

        while v > 0:
            dig = "1" if v % 2 == 1 else "0"

            # prepend digits b/c we processed lowest bit first
            s = dig + s

            v //= 2

        return s

    def add_binary(self, a: str, b: str) -> str:
        """."""
        a_v = self.from_binary_str(a)
        b_v = self.from_binary_str(b)

        return self.to_binary_str(a_v + b_v)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
