"""."""

from textwrap import dedent

from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestTowerBreakers(StdinExecutor, OutputFileWriter):
    def test_tower_breakers_basic(self) -> None:
        sin = dedent(r"""2
                         2 2
                         1 4""")
        self.exec(self.from_mdye_hackerrank("solution_tower_breakers.py"), sin)

        assert self._read_output_lines(stripped=True) == ["2", "1"]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
