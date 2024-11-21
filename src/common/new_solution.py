"""."""

import argparse
import os
import sys
from enum import Enum
from pathlib import Path
from typing import List

_indent = "    "
_vim_modeline = "# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4"


class SolutionKind(Enum):
    EULER = "euler"
    LEETCODE = "leetcode"


class SolutionContent:
    def __init__(self, mod_dir: Path, kind: SolutionKind, number: int):
        """."""
        self._kind = kind
        self._number = number

        self._impl_outp = Path(mod_dir, f"solution_{number}.py")
        self._test_outp = Path(mod_dir, "test", f"test_solution_{number}.py")

        self._impl_content = self._render_templ(self._impl_templ())
        self._test_content = self._render_templ(self._test_templ(self._kind, self._number))

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
    def _impl_templ(cls) -> List[str]:
        return [
            "",
            "class Solution:",
            f"{_indent}pass",
            "",
            "",
            _vim_modeline,
            "",
        ]

    @classmethod
    def _test_templ(cls, kind: SolutionKind, solnum: int) -> List[str]:
        lines = []

        lines += ["", "import pytest", ""]

        if kind == SolutionKind.LEETCODE:
            lines += [
                f"from mdye_{kind.value}.solution_{solnum} import Solution",
                "",
                "",
                "# makes a Solution object b/c that's how leetcode rolls",
                """@pytest.fixture(scope="module")""",
                "def sol():",
                f"{_indent}yield Solution()",
                "",
                "",
                f"def test_solution_{solnum}_basic(sol: Solution):",
                f"{_indent}assert False",
            ]

        elif kind == SolutionKind.EULER:
            lines += [
                f"from mdye_{kind.value}.solution_{solnum} import solve",
                "",
                "def test_solution():",
                f"{_indent}tassert False",
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
            f"{self._kind=}, {self._number=}, {self._impl_outp=}, {self._test_outp=}"
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
    parser.add_argument("-n", "--number", action="store", type=int, required=True)

    args = parser.parse_args()
    kind = SolutionKind(args.kind)

    mod_dir = Path(Path(__file__).parent, "..", f"mdye_{kind.value}").resolve()

    content = SolutionContent(mod_dir, kind, args.number)
    content.write()

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
