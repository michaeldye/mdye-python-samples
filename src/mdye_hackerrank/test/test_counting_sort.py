"""."""

from textwrap import dedent

from mdye_hackerrank.solution_counting_sort import counting_sort
from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestComparisonSort(StdinExecutor, OutputFileWriter):
    def test_counting_sort_stdin_stdout(self) -> None:
        sin = dedent(r"""100
                         63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33""")
        self.exec(self.from_mdye_hackerrank("solution_counting_sort.py"), sin)

        assert (
            self._read_val()
            == "0 2 0 2 0 0 1 0 1 2 1 0 1 1 0 0 2 0 1 0 1 2 1 1 1 3 0 2 0 0 2 0 3 3 1 0 0 0 0 2 2 1 1 1 2 0 2 0 1 0 1 0 0 1 0 0 2 1 0 1 1 1 0 1 0 1 0 2 1 3 2 0 0 2 1 2 1 0 2 2 1 2 1 2 1 1 2 2 0 3 2 1 1 0 1 1 1 0 2 2"
        )

    def test_counting_sort_freq_array(self) -> None:
        arr = [1, 9, 6, 9, 12]
        expected = [0, 1, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 1]

        # output will always be length == 100 so we take just the head of the return that we want
        assert counting_sort(arr)[0 : len(expected)] == expected


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
