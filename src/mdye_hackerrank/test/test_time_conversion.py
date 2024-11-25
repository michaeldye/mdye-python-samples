"""."""

import os
import shutil
from pathlib import Path

from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestTimeConversion(StdinExecutor, OutputFileWriter):
    output_envvar = "OUTPUT_PATH"

    def setup_method(self) -> None:
        super().setup_method()

        self.module = self.from_mdye_hackerrank("solution_time_conversion.py")

        tmpfile = Path(self.tmpdir, "out")
        os.environ[self.output_envvar] = str(tmpfile)

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
