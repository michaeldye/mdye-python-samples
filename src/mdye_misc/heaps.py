#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import Optional

##
# Heap properties:
# - usually a "complete" binary tree (and this one is)
#   - this makes it so we can store one in an array, really compactly
#     - For each index i, element arr[i] has children at arr[2i + 1] and arr[2i + 2], and the parent at arr[floor( ( i - 1 )/2 )].

# - either a minheap or maxheap; this is the latter so,
#   - any Node is greater than child nodes (max heap property)

# * most efficient implementation of a priority queue is a Heap, but note that a useful queue has unknown qty of elements up front so that necessitates using a dynamic array

##
# More about binary tree properties:
# - "complete": all levels of tree filled except perhaps the bottom, and it's filled from left-to-right
# - "balanced": difference between subtrees never exceeding 1 (but could be either related to height-balancedness or weight-balancedness, the former being more common). The AVL tree is a height-balanced BST
# - every complete binary tree is also balanced (w/r/t height?), but not the converse


class MaxHeap:
    _back = []

    def __init__(self):
        pass

    def insert(self, value: int) -> Optional[None]:
        self._back.append(value)
        # always heapify after insert
        self._heapify(len(self._back) - 1)

    def extract_max(self) -> Optional[int]:
        if len(self._back) == 0:
            return None

        res = self._back[0]

        if len(self._back) > 1:
            self._back[0] = self._back[-1]

        self._back = self._back[0:-1]
        self._heapify_down(0)
        return res

    def _heapify_down(self, pos: int) -> None:
        def larger(c: int, al: int) -> int:
            if len(self._back) > al and self._back[al] > self._back[c]:
                return al
            return c

        while pos < len(self._back):
            la = larger(pos, pos * 2 + 1)
            la = larger(la, pos * 2 + 2)

            if la == pos:
                return

            self._swap(pos, la)
            pos = la

    def _heapify(self, pos: int) -> None:

        while (pos - 1) // 2 >= 0:
            parent = pos // 2
            # determine if the starting index (pos) and its parent need swapping
            if self._back[pos] > self._back[parent]:
                # element at pos is greater than its parent; swappin time!
                self._swap(pos, parent)
            pos = parent

    def _swap(self, x: int, y: int) -> None:
        tmp = self._back[x]
        self._back[x] = self._back[y]
        self._back[y] = tmp

    def __str__(self) -> str:
        return str(self._back)


if __name__ == "__main__":
    h = MaxHeap()
    h.insert(5)
    h.insert(6)
    h.insert(6)
    h.insert(7)
    h.insert(7)
    h.insert(1)
    h.insert(12)
    h.insert(19)
    h.insert(32)
    h.insert(2)
    h.insert(1)
    h.insert(22)
    h.insert(42)
    h.insert(19)
    h.insert(65)

    pq = []

    for _ in range(len(h._back)):
        largest = h.extract_max()
        if len(pq) > 1:
            assert largest <= pq[-1]
        pq.append(largest)

    print("priority order after popping top of heap each time:")
    print(pq)

    print("done")
    sys.exit(0)
