from textwrap import dedent

from mdye_hackerrank.testing_support import StdinExecutor


class TestPySetDiscardRemovePop(StdinExecutor):
    @classmethod
    def setup_method(cls) -> None:
        cls.module = cls.from_mdye_hackerrank("py_set_discard_remove_pop.py")

    def test_py_set_discard_remove_pop(self) -> None:
        input_lines = dedent(r"""9
                                 1 2 3 4 5 6 7 8 9
                                 10
                                 pop
                                 remove 9
                                 discard 9
                                 discard 8
                                 remove 7
                                 pop
                                 discard 6
                                 remove 5
                                 pop
                                 discard 5""")

        assert self.exec(self.module, input_lines) == "4"
