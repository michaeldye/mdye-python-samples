"""."""

from mdye_hackerrank.solution_grid_challenge import gridChallenge
from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor

YES = "YES"
NO = "NO"


class TestGridChallenge(StdinExecutor, OutputFileWriter):
    def test_grid_challenge_2x2_sort_one(self) -> None:
        assert gridChallenge(["kc", "iu"]) == YES

    def test_grid_challenge_2x2_bad(self) -> None:
        assert gridChallenge(["cg", "cc"]) == NO

    def test_grid_challenge_basic(self) -> None:
        sin = r"""2
                  2
                  kc
                  iu
                  3
                  uxf
                  vof
                  hmp"""
        self.exec(self.from_mdye_hackerrank("solution_grid_challenge.py"), sin)

        assert [s.strip() for s in self._read_output_lines()] == ["YES", "NO"]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
