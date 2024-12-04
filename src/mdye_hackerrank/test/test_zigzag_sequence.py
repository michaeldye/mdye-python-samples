"""."""

from mdye_hackerrank.testing_support import StdinExecutor


class TestZigzagSequence(StdinExecutor):
    def test_zigzag_sequence_basic(self) -> None:
        sin = r"""1
                  7
                  1 2 3 4 5 6 7"""
        assert (
            self.exec(self.from_mdye_hackerrank("solution_zigzag_sequence.py"), sin)
            == "1 2 3 7 6 5 4"
        )


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
