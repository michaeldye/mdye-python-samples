"""."""


class Solution:
    # O(n**2) time complexity b/c we have to iterate over all n letters as well
    # as compare all letters in substrings of s with s, which requires further
    # iteration. Unfortunately, our shortcut to not process past half of len(s)
    # doesn't improve efficiency estimate

    # Better approaches include Rabin-Carp on discovered substring lengths and
    # KMP.

    def repeated_substring_pattern(self, s: str) -> bool:
        """."""
        # form substrings (starting with just the first letter in s) of increasing size
        # up to len(s) and test that substring against the given s; return True on
        # first occurrence of success

        # never need to move start index (0) b/c we must form a complete s

        # only have to form substrings up to 1/2 the length of s or they can't be appended
        # and form s
        for ch_end in range(1, (len(s) // 2) + 1):
            sub = s[:ch_end]

            if len(s) % len(sub) != 0 or s[-1] != s[-1]:
                continue  # skip trying this substring b/c it's inviable

            # a little less manual than perhaps expected, but whatever ...
            if sub * (len(s) // len(sub)) == s:
                return True

        return False


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
