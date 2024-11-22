#!/usr/bin/env python3
"""."""

import random
import string
import sys
from typing import Callable, List, Optional

from mdye_misc.linked_list import LinkedList, Node


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

    def __init__(self, size: int, hash_fn: Optional[Callable[[str], int]] = None):
        """."""
        if not hash_fn:
            self._hash = self._hash_division
        else:
            self._hash = hash_fn

        self._size = size
        self._table = [LinkedList() for _ in range(size)]

    def insert(self, val: str) -> None:
        """."""
        h = self._hash(val)

        node = self._get(val, h)
        if not node:
            # prepend b/c that's O(1) in a linkedlist
            self._table[h].prepend(Node(val))

    def _get(self, val: str, h: Optional[int] = None) -> Optional[Node]:
        if not h:
            h = self._hash(val)

        if (n := self._table[h].search(val)) is not None:
            return n

        return None

    def get(self, val: str) -> Optional[str]:
        """."""
        n = self._get(val)
        if n is not None:
            return n.val

        return None

    def _hash_knuth_variant(self, item: str) -> int:
        # using h(k) = k(k + 3) mod m, where k is the key (int value if item)
        # and m is the size of the hash table

        k = self._str_to_int(item)  # use python's built-in hash to get an int value from our item
        return (k * (k + 3)) % self._size

    def _hash_division(self, item: str) -> int:
        k = self._str_to_int(item)
        return k % self._size

    @staticmethod
    def _str_to_int(item: str) -> int:
        # python's hash() function is not deterministic across runs so we made our own for simplicity
        val = 0

        for ch in item:
            val += ord(ch)

        return val

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

    # now fill one up with a lot of randomized string content
    table2 = HashTable(64)

    for w in range(300):
        w = "".join(
            [random.choice(string.ascii_letters + string.digits) for _ in range(2, 29)]  # noqa: S311
        )
        table2.insert(w)

    sys.exit(0)
