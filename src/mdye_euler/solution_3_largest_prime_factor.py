# -*- coding: utf-8 -*-

import math
from typing import List, Callable

# Need to repeatedly dimish given int, n, by smallest prime found that is
# greater than all previous until no prime factors are left. The last factor
# will be the largest prime factor. Note that prime factors of a number (n)
# will be in range [2, sqrt(n) + 1]


def primes_range(st: int, end: int) -> List[int]:
    # clipped from internet b/c I didn't want to sieve by myself

    sieve = [True] * end
    sieve[0] = False  # Zero and one are not prime numbers.
    sieve[1] = False

    # Create the sieve:
    for i in range(st, end):
        pointer = i * 2
        while pointer < end:
            sieve[pointer] = False
            pointer += i

    # Compile the list of primes:
    primes = []
    for i in range(end):
        if sieve[i]:
            primes.append(i)

    return primes


def lpf(n: int) -> int:
    prime_range = range(2, math.floor(math.sqrt(n)) + 1)
    pfn = prime_finder(list(prime_range))

    while True:
        prime = pfn(n)

        if prime == n:
            return n

        n //= prime


def prime_finder(primes: List[int]) -> Callable[[int], int]:
    last_ix = 0

    def prime_fn(n: int):
        nonlocal last_ix  # this is necessary b/c we rebind the variable below and the compiler doesn't know it's closed over above?
        for ix, div in enumerate(primes[last_ix:]):
            if n % div == 0:
                last_ix = ix + 1
                return div
        return None

    return prime_fn

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
