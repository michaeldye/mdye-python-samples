from textwrap import dedent

from mdye_hackerrank.testing_support import StdinExecutor


class TestNoIdea(StdinExecutor):
    @classmethod
    def setup_method(cls) -> None:
        cls.module = cls.from_mdye_hackerrank("py_set_add.py")

    def test_py_set_add(self) -> None:
        input_lines = dedent(r"""7
                           UK
                           China
                           USA
                           France
                           New Zealand
                           UK
                           France""")

        assert self.exec(self.module, input_lines) == "5"
