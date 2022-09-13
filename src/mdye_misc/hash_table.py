#!/bin/env python3

import sys
import string
import random

from typing import Optional, List, Callable
from linked_list import Node, LinkedList


class HashTable:

    # Backing data structure is list with "buckets" of linkedlists; when
    # inserting, it's necessary to traverse the LinkedList looking for
    # duplicate values. This is part of a chaining hash strategy (instead of
    # the linear probing option, which kinda sucks)

    # Effectiveness of the hash table at providing O(n) lookup time depends
    # on the performance of our hashing function for the stored data. We are
    # storing strings that are to be psuedo-randomly generated with small
    # variability in length; a content-based hash will work ok for this.

    _table: List[LinkedList]
    _size: int
    _hash: Callable[[str], int]

    def __init__(self, size: int, hash_fn: Callable[[str], int] = None):
        if not hash_fn:
            self._hash = self._hash_division
        else:
            self._hash = self._hash_knuth_variant

        self._size = size
        self._table = [LinkedList() for _ in range(size)]

    def insert(self, val: str) -> None:
        h = self._hash(val)

        if not self.get(val, h):
            self._table[h].prepend(Node(val))

    def get(self, val: str, h: int = None) -> Optional[str]:
        if not h:
            h = self._hash(val)

        return self._table[h].search(val)

    def _hash_knuth_variant(self, item: str) -> int:
        # using h(k) = k(k + 3) mod m, where k is the key (int value if item)
        # and m is the size of the hash table

        k = hash(item)  # use python's built-in hash to get an int value from our item
        return (k * (k + 3)) % self._size

    def _hash_division(self, item: str) -> int:
        k = hash(item)
        return k % self._size

    def __str__(self) -> str:
        sb = ""

        for ix, b in enumerate(self._table):
            sb += f"\n{ix}: {b}"

        return sb


if __name__ == "__main__":
    # bad size, whatevs
    table = HashTable(4)
    table.insert("foo")
    table.insert("goog")
    table.insert("mm")
    table.insert("mm")

    assert not table.get("zoo")
    assert table.get("foo") == "foo"

    print("Tiny table:")
    print(table)

    # now fill one up with a lot of randomized string content
    table2 = HashTable(64)

    for w in range(300):
        w = "".join(
            [random.choice(string.ascii_letters + string.digits) for _ in range(2, 29)]
        )
        table2.insert(w)

    print(table2)
    print("done")

    sys.exit(0)
