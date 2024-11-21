"""."""


class Solution:
    def are_almost_equal(self, s1: str, s2: str) -> bool:
        """."""
        s1_mismatch_ixes = []

        for ix, c in enumerate(s1):
            if c != s2[ix]:
                if len(s1_mismatch_ixes) >= 2:
                    return False

                s1_mismatch_ixes.append(ix)

        size = len(s1_mismatch_ixes)
        if size == 0:
            return True

        if size == 2:
            sx = s1_mismatch_ixes[0]
            fx = s1_mismatch_ixes[1]

            if s1[sx] == s2[fx] and s1[fx] == s2[sx]:
                return True

        return False


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
