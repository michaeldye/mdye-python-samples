"""."""

from mdye_hackerrank.solution_caeser_cipher import caesarCipher
from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestCaeserCipher(StdinExecutor, OutputFileWriter):
    def test_caesar_cipher_fn(self) -> None:
        s = "middle-Outz"
        k = 2

        assert caesarCipher(s, k) == "okffng-Qwvb"

    def test_caeser_cipher_basic(self) -> None:
        sin = r"""11
                  middle-Outz
                  2"""
        self.exec(self.from_mdye_hackerrank("solution_caeser_cipher.py"), sin)

        assert self._read_val() == "okffng-Qwvb"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
