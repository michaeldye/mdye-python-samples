from textwrap import dedent

from mdye_hackerrank.testing_support import StdinExecutor


class TestPySetAdd(StdinExecutor):
    @classmethod
    def setup_method(cls) -> None:
        cls.module = cls.from_mdye_hackerrank("plus_minus.py")

    @classmethod
    def _lines_as_arr(cls, data: str) -> list[str]:
        return data.split()

    def test_plus_minus(self) -> None:
        stdin = dedent(r"""6
                           -4 3 -9 0 4 1""")

        out_vals = self._lines_as_arr(r"""0.500000
                                          0.333333
                                          0.166667""")

        assert self._lines_as_arr(self.exec(self.module, stdin)) == out_vals
