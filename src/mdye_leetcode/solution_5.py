
class Solution:

    def fromMiddles(self, mid_f: int, mid_s: int, s: str) -> (int, int):
        dis = start = end = 0

        # condition ensures we don't point beyond the beginning of the word
        while dis <= mid_f:

            pstart = mid_f - dis
            pend = mid_s + dis

            if len(s) - pend == 0:
                break  # reached end of word

            if s[pstart] == s[pend]:
                end = pend
                start = pstart
            else:
                break

            dis += 1

        return start, end

    def longestPalindrome(self, s: str) -> str:

        longest = ""

        for ix in range(len(s)):
            st, en = self.fromMiddles(ix, ix, s)

            # if we're not on the last letter, consider an even palindrome
            if ix + 1 <= len(s):
                dst, den = self.fromMiddles(ix, ix + 1, s)
                if den - dst > en - st:
                    st = dst
                    en = den

            if en - st + 1 > len(longest):
                longest = s[st: en + 1]

        return longest


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
