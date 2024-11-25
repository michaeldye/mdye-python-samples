"""."""

from mdye_hackerrank.testing_support import StdinExecutor


class TestMinMaxSum(StdinExecutor):
    @classmethod
    def setup_method(cls) -> None:
        cls.module = cls.from_mdye_hackerrank("solution_min_max_sum.py")

    def test_min_max_sum_basic(self) -> None:
        assert self.exec(self.module, "1 2 3 4 5") == "10 14"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
