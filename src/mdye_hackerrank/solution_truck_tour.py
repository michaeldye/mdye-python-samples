"""."""

import os


def truckTour(petrolpumps: list[list[int]]) -> int:  # noqa: D103, N802
    def can_complete(starting: int) -> bool:
        fuel_qty = 0
        for offset in range(len(petrolpumps)):
            curr = (starting + offset) % len(petrolpumps)  # wrap to front

            pump = petrolpumps[curr]
            fuel_qty += pump[0]
            fuel_qty -= pump[1]

            if fuel_qty < 0:
                # busted, we can't reach next station from this station
                return False
        return True

    for starting in range(len(petrolpumps)):
        if can_complete(starting):
            return starting

    raise RuntimeError("Failed to find proper starting station")


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")  # noqa: SIM115

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    fptr.write(str(result) + "\n")

    fptr.close()

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
