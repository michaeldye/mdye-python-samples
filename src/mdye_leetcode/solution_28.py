"""."""


class Solution:
    def str_str(self, haystack: str, needle: str) -> int:
        """."""
        # ix is the index for the letter in haystack under investigation,
        # nix is the index for the letter in needle,
        # and stix is the start index into haystack at which we started
        # matching against ix and nix.

        # This is important because when we fail to make a complete match,
        # we need to reset ix to stix

        ix = nix = stix = 0

        while ix < len(haystack):
            if haystack[ix] == needle[nix]:
                if nix == 0:
                    stix = ix

                nix += 1

                if nix == len(needle):
                    # true when we've found the last letter in needle matches a substring of haystack
                    return stix
            else:
                # tricky bit: must set ix to stix only when we have just found
                # a failed character match in a sequence, not while iterating
                # through haystack's chars and finding no matches
                if nix != 0:
                    ix = stix  # ix will get incremented later

                nix = 0

            ix += 1

        return -1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
