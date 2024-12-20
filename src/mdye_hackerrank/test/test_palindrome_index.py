"""."""

from textwrap import dedent

from mdye_hackerrank.solution_palindrome_index import palindrome_index
from mdye_hackerrank.testing_support import StdinExecutor


class TestPalindromeIndex(StdinExecutor):
    def test_palindrome_empty(self) -> None:
        assert palindrome_index("") == -1

    def test_palindrome_last_ch(self) -> None:
        assert palindrome_index("aaab") == 3

    def test_palindrome_already_odd(self) -> None:
        assert palindrome_index("aaa") == -1

    def test_palindrome_already_even(self) -> None:
        assert palindrome_index("bb") == -1

    def test_palindrome_index_basic(self) -> None:
        sin = dedent(r"""3
                         aaab
                         baa
                         aaa""")
        sout = self.exec(self.from_mdye_hackerrank("solution_palindrome_index.py"), sin)
        assert sout.split() == ["3", "0", "-1"]


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
