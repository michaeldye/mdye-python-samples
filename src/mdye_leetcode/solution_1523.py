"""."""


class Solution:
    def count_odds(self, low: int, high: int) -> int:
        """."""
        return self.count_odds_mathy(low, high)

    def count_odds_mathy(self, low: int, high: int) -> int:
        """."""
        range_qty = (high - low) // 2  # b/c high is inclusive we don't subtract 1

        if low % 2 == 1 or high % 2 == 1:
            range_qty += 1

        return range_qty


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
