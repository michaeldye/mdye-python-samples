#!/usr/bin/env python3

"""problem: http://www.hackerrank.com/challenges/no-idea/problem.

Input:

3 2 # counts of n, m
1 5 3 # n vals
3 1 # set A
5 7 # set B

Points to remember:

* input() <-- read next line from stdin
* split() <-- without arg, will split on whitespace
* instead of lambda x: int(x), just "int" (fn name)
* The implementation was too slow before replacing the list comp. -> set
  conversion and delaying iteration over n vals (with no storage as list first)
"""


def _read_ints(expected_len: int) -> list[int]:
    d = [int(x) for x in input().split()]
    assert len(d) == expected_len
    return d

def _read_sets(expected_len: int) -> set[int]:
    # b/c we think this is faster than the list comp to set way
    raw_spl = input().split()
    c = set()
    for v in raw_spl:
        c.add(int(v))

    assert len(c) == expected_len
    return c


sizes = _read_ints(2)
n_size, m_size = sizes

n_strs = input().split()
a = _read_sets(m_size)
b = _read_sets(m_size)

happy = 0

# do the counting
for val in n_strs:
    i = int(val)
    if i in a:
        happy += 1
    if i in b:
        happy -= 1

print(happy)
