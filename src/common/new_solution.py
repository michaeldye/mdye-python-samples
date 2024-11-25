"""."""

import argparse
import os
import sys
from enum import Enum
from pathlib import Path
from typing import List

_indent = "    "
_vim_modeline = "# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4"


def to_camel(snake_case: str) -> str:
    """."""
    nd = snake_case.split("_")
    assert len(nd) > 0

    def j(*parts: str) -> str:
        return "".join(parts)

    def cap(word: str) -> str:
        return j(word[0].upper(), word[1:])

    return j(*[cap(w) for w in nd])


class SolutionKind(Enum):
    EULER = "euler"
    LEETCODE = "leetcode"
    HACKERRANK = "hackerrank"


class SolutionContent:
    def __init__(self, mod_dir: Path, kind: SolutionKind, name: str):
        """."""
        self._kind = kind
        self._name = name

        self._impl_outp = Path(mod_dir, f"solution_{name}.py")
        self._test_outp = Path(mod_dir, "test", f"test_{name}.py")

        self._impl_content = self._render_templ(self._impl_templ(self._kind))
        self._test_content = self._render_templ(self._test_templ(self._kind, self._name))

    def write(self) -> None:
        """."""
        self._safe_write(self._impl_outp, self._impl_content)
        self._safe_write(self._test_outp, self._test_content)

    @staticmethod
    def _safe_write(outf: Path, content: str) -> None:
        if outf.exists():
            raise RuntimeError(f"{outf} already exists and mustn't")

        with open(outf, "w") as ou:
            ou.write(content)
            ou.flush()

    @staticmethod
    def _render_templ(lines: List[str]) -> str:
        return os.linesep.join(lines)

    @classmethod
    def _impl_templ(cls, kind: SolutionKind) -> List[str]:
        lines = ['"""."""', "", "import sys", ""]

        if kind == SolutionKind.HACKERRANK:
            lines += ['if __name__ == "__main__":', f"{_indent}sys.exit(4)"]
        else:
            lines += [
                "",
                "class Solution:",
                f"{_indent}pass",
            ]

        lines += [
            "",
            "",
            _vim_modeline,
            "",
        ]

        return lines

    @classmethod
    def _test_templ(cls, kind: SolutionKind, name: str) -> List[str]:
        lines = ['"""."""', ""]

        # N.B. if this templating gets much more silly we need to switch to a
        # proper language generator

        if kind == SolutionKind.LEETCODE:
            lines += [
                f"from mdye_{kind.value}.solution_{name} import Solution",
                "",
                "",
                "# makes a Solution object b/c that's how leetcode rolls",
                """@pytest.fixture(scope="module")""",
                "def sol():",
                f"{_indent}yield Solution()",
                "",
                "",
                f"def test_solution_{name}_basic(sol: Solution):",
                f'{_indent}raise AssertionError("Unimplemented")',
            ]

        elif kind == SolutionKind.EULER:
            lines += [
                f"from mdye_{kind.value}.solution_{name} import solve",
                "",
                "",
                "def test_solution():",
                f'{_indent}raise AssertionError("Unimplemented")',
            ]

        elif (
            kind == SolutionKind.HACKERRANK
        ):  # TODO: differentiate those that write to output files and those that send stdout
            lines += [
                "from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor",
                "",
                "",
                f"class Test{to_camel(name)}(StdinExecutor, OutputFileWriter):",
                "",
                f"{_indent}def test_{name}_basic(self) -> None:",
                f'{_indent}{_indent}sin = r""""""' "",
                f'{_indent}{_indent}self.exec(self.from_mdye_hackerrank("solution_{name}.py"), sin)',
                "",
                f'{_indent}{_indent}assert self._read_val() == "foo"',
            ]

        lines += [
            "",
            "",
            _vim_modeline,
            "",
        ]

        return lines

    def __str__(self) -> str:
        def _content_with_seps(name: str, content: str) -> str:
            return str(
                f"\n----------- {name} ----------------\n{str(content)}\n-----------------------------------------------"
            )

        return str(
            f"{self._kind=}, {self._name=}, {self._impl_outp=}, {self._test_outp=}"
            f"\n{_content_with_seps('implementation file content', self._impl_content)}"
            f"\n{_content_with_seps('test file content', self._test_content)}"
        )


def main() -> None:
    """."""
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-k",
        "--kind",
        action="store",
        choices=[k.value for k in SolutionKind],
        type=str,
        required=True,
    )
    parser.add_argument(
        "-sn",
        "--snake-case-name",
        action="store",
        type=str,
        required=True,
        help="Python module-safe name w/ underscores",
    )

    args = parser.parse_args()
    kind = SolutionKind(args.kind)

    mod_dir = Path(Path(__file__).parent, "..", f"mdye_{kind.value}").resolve()

    content = SolutionContent(mod_dir, kind, args.snake_case_name)
    content.write()

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
