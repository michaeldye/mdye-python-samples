"""test_support.

Support class for testing hackerrank solutions in a stable project structure
that supports execution from vscode and Make.
"""

import subprocess
import sys
from pathlib import Path


class StdinExecutor:
    @staticmethod
    def from_mdye_hackerrank(module_name: str) -> str:
        """."""
        p = Path(__file__).parent
        f = Path(p, module_name)
        assert f.exists()
        return str(f)

    def exec(self, module_path: str, sin: str) -> str:
        """."""
        # Use from_mdye_hackerrank(name) to load module from common test dir
        # that contains this support module.

        # We maintain sys.stderr support here b/c we want to be able to do
        # simple debug w/ things like print(f"{n=}", file=sys.stderr) in puzzle
        # code (note that to see such output in pytest you must execute with
        # -s (a shortcut for --capture=no)
        p = subprocess.run(
            [f"python {module_path}"],
            shell=True,
            input=sin,
            text=True,
            stdout=subprocess.PIPE,
            stderr=sys.stderr,
        )

        if p.returncode != 0:
            n = Path(module_path).name
            raise AssertionError(f"Module named {n} exited with non-zero code: {p.returncode}")

        return p.stdout.strip()
