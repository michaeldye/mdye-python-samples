"""."""

import os
import shutil
from pathlib import Path
from tempfile import mkdtemp

from mdye_hackerrank.testing_support import StdinExecutor


class TestTimeConversion(StdinExecutor):
    envvar_name = "OUTPUT_PATH"

    @classmethod
    def setup_method(cls) -> None:
        cls.module = cls.from_mdye_hackerrank("solution_time_conversion.py")
        cls.tmpdir = mkdtemp()

        tmpfile = Path(cls.tmpdir, "out")
        os.environ[cls.envvar_name] = str(tmpfile)

    @classmethod
    def teardown_method(cls) -> None:
        if cls.tmpdir is not None:
            shutil.rmtree(cls.tmpdir)

        os.environ.pop(cls.envvar_name)

    def _read_val(self) -> str:
        with Path(os.environ[self.envvar_name]).open("r", encoding="utf-8") as inf:
            return inf.readlines()[0].rstrip()

    def test_time_conversion_basic(self) -> None:
        self.exec(self.module, "07:05:45PM")
        assert self._read_val() == "19:05:45"

    def test_time_conversion_am(self) -> None:
        self.exec(self.module, "06:40:03AM")
        assert self._read_val() == "06:40:03"

    def test_time_conversion_pm(self) -> None:
        self.exec(self.module, "03:12:00PM")
        assert self._read_val() == "15:12:00"

    def test_time_conversion_leading(self) -> None:
        self.exec(self.module, "12:12:11PM")
        assert self._read_val() == "12:12:11"

    def test_time_conversion_twelve_am(self) -> None:
        self.exec(self.module, "12:10:00AM")
        assert self._read_val() == "00:10:00"

    def test_time_conversion_twelve_pm(self) -> None:
        self.exec(self.module, "12:45:54PM")
        assert self._read_val() == "12:45:54"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
