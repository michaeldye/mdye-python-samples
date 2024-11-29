from textwrap import dedent

from mdye_hackerrank.testing_support import StdinExecutor


class TestNoIdea(StdinExecutor):
    def test_no_idea_stdin(self):
        sin = dedent(r"""3 2
                         1 5 3
                         3 1
                         5 7""")

        assert self.exec(self.from_mdye_hackerrank("no_idea.py"), sin) == "1"
