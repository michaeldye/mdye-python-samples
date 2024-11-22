import subprocess
import sys
from pathlib import Path
from textwrap import dedent


class TestNoIdea:
    @staticmethod
    def _from_mdye_hackerrank(fname: str) -> str:
        p = Path(__file__).parent.parent
        f = Path(p, fname)
        assert f.exists()
        return str(f)

    def _exec(self, sin: str) -> str:
        mod = self._from_mdye_hackerrank("no_idea.py")

        p = subprocess.run(
            [f"python {mod}"],
            shell=True,
            input=sin,
            text=True,
            stdout=subprocess.PIPE,
            stderr=sys.stderr,
        )
        return p.stdout.strip()

    def test_no_idea_stdin(self):
        sin = dedent(r"""3 2
                         1 5 3
                         3 1
                         5 7""")

        out = self._exec(sin)
        assert out == "1"
