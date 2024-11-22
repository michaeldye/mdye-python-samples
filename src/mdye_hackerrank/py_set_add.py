"""."""

# problem: https://www.hackerrank.com/challenges/py-set-add/problem

import sys

if __name__ == "__main__":
    n = int(input())

    ct = 0
    countries = set()
    for co in sys.stdin.readlines():
        ct += 1

        countries.add(co.strip())

    assert ct == n
    print(len(countries))
