def solve(limit: int) -> int:
    prevprev = prev = ix = total = 0

    while True:
        if ix <= 2:
            curr = ix
        else:
            curr = prev + prevprev

        prevprev = prev
        prev = curr

        if curr > limit:
            return total
        elif curr % 2 == 0:
            total += curr

        ix += 1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
