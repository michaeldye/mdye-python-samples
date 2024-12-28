"""."""

from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestMergedSortedLinkedLists(StdinExecutor, OutputFileWriter):
    def test_merged_sorted_linked_lists_basic(self) -> None:
        sin = r"""1
                  3
                  1
                  2
                  3
                  2
                  3
                  4"""

        self.exec(self.from_mdye_hackerrank("solution_merged_sorted_linked_lists.py"), sin)
        assert self._read_output_lines()[0].strip() == "1 2 3 3 4"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
