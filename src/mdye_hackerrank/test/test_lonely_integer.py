"""."""

from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestLonelyInteger(StdinExecutor, OutputFileWriter):
    def test_lonely_integer_basic(self) -> None:
        sin = r""""""
        self.exec(self.from_mdye_hackerrank("solution_lonely_integer.py"), sin)

        assert self._read_val() == "foo"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
