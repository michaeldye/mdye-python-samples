"""."""

from textwrap import dedent

from mdye_hackerrank.solution_new_year_chaos import minimumBribes
from mdye_hackerrank.testing_support import StdinExecutor


class TestNewYearChaos(StdinExecutor):
    def test_minimumBribes_transitive_bribe(self, capsys) -> None:  # noqa: N802
        q = [1, 2, 5, 3, 7, 8, 6, 4]

        minimumBribes(q)
        assert capsys.readouterr().out.strip() == "7"

    def test_minimumBribes_too_chaotic(self, capsys) -> None:  # noqa: N802
        q = [5, 1, 2, 3, 7, 8, 6, 4]

        minimumBribes(q)
        assert capsys.readouterr().out.strip() == "Too chaotic"

    def test_new_year_chaos_basic(self) -> None:
        sin = dedent(r"""2
                         8
                         5 1 2 3 7 8 6 4
                         8
                         1 2 5 3 7 8 6 4""")
        raw_output = self.exec(self.from_mdye_hackerrank("solution_new_year_chaos.py"), sin)

        assert raw_output.split("\n") == ["Too chaotic", "7"]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
