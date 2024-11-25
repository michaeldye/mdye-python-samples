from textwrap import dedent

from mdye_hackerrank.testing_support import StdinExecutor


def _lines_as_arr(data: str) -> list[str]:
    return data.split()


class TestPySetAdd(StdinExecutor):
    def test_plus_minus(self) -> None:
        stdin = dedent(r"""6
                           -4 3 -9 0 4 1""")

        out_vals = _lines_as_arr(r"""0.500000
                                     0.333333
                                     0.166667""")

        assert (
            _lines_as_arr(self.exec(self.from_mdye_hackerrank("plus_minus.py"), stdin)) == out_vals
        )
