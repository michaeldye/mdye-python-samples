"""."""

from mdye_hackerrank.solution_matrix_flip import flippingMatrix
from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestMatrixFlip(StdinExecutor, OutputFileWriter):
    def test_matrix_flip_flipping_matrix_sums(self) -> None:
        matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

        assert flippingMatrix(matrix) == 414

    def test_matrix_flip_basic(self) -> None:
        sin = r"""1
                  2
                  112 42 83 119
                  56 125 56 49
                  15 78 101 43
                  62 98 114 108"""

        self.exec(self.from_mdye_hackerrank("solution_matrix_flip.py"), sin)

        assert self._read_val() == "414"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
