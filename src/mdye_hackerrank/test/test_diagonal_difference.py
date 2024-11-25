"""."""

from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestDiagonalDifference(StdinExecutor, OutputFileWriter):

    def test_diagonal_difference_basic(self) -> None:
        sin = r"""3
                  11 2 4
                  4 5 6
                  10 8 -12"""

        self.exec(self.from_mdye_hackerrank("solution_diagonal_difference.py"), sin)

        assert self._read_val() == "15"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
