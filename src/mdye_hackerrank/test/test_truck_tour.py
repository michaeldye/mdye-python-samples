"""."""

from mdye_hackerrank.solution_truck_tour import truckTour
from mdye_hackerrank.testing_support import OutputFileWriter, StdinExecutor


class TestTruckTour(StdinExecutor, OutputFileWriter):
    def test_truckTour_first(self) -> None:  # noqa: N802
        assert truckTour([[1, 5], [10, 3], [3, 4]]) == 1

    def test_truck_tour_basic(self) -> None:
        sin = r"""3
                  1 5
                  10 3
                  3 4"""
        self.exec(self.from_mdye_hackerrank("solution_truck_tour.py"), sin)

        assert self._read_val() == "1"


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
