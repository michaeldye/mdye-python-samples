from textwrap import dedent

from mdye_hackerrank.testing_support import StdinExecutor


class TestNoIdea(StdinExecutor):
    @classmethod
    def setup_method(cls) -> None:
        cls.module = cls.from_mdye_hackerrank("no_idea.py")

    def test_no_idea_stdin(self):
        sin = dedent(r"""3 2
                         1 5 3
                         3 1
                         5 7""")

        out = self.exec(self.module, sin)
        assert out == "1"
