#!/usr/bin/env python3

## a demo mutable array list in python built on the ctypes.array type
# 
# append: worst case: O(N) (because we have to reallocate array and copy (extend)), but it's amortized cost so we can generalize to O(1)
# prepend: (not implemented in this class, but making a new ds with prepended value would be O(N) b/c an extend is required
# search: O(N)
# get by index: O(1)

# good for: cases where you append data to the ds and you look up by index

# Tip: in the repl, you can get the docs for a variable's type with:
# >>> import ctypes
# >>> o = (ctypes.c_long * 2)(*range(2))
# >>> help(o)

import sys

import ctypes
from ctypes import cast

class LongArrayList(object):
    # uses a backing array that can only store signed longs (4 bytes in length, so 32bits - 1 bit for signing leaves -2,147,483,648 to 2,147,483,647 as range)

    _used_ct = 0
    
    def __init__(self, size: int):
        self._back = self._new_backing(size)
        assert len(self._back) == size

    def __len__(self) -> int:
        return self._used_ct

    def __getitem__(self, pos: int) -> int:
        if pos > self._used_ct or pos < 0:
            raise IndexError()
        else:
            return self._back[pos]

    @staticmethod
    def _new_backing(size: int) -> ctypes.Array:
        # type is <class '_ctypes.PyCArrayType'>
        seq = (ctypes.c_long * size)
        return seq(*[0]) # this step fills the fucker which is necessary to get it to act like a ctypes.Array

    def _expand(self, size: int) -> None:
        # does resize and copy, sets self._back
        old = self._back
        self._back = self._new_backing(size)
        for ix in range(self._used_ct):
            self._back[ix] = old[ix]


    def add(self, val: int) -> None:
        if self._used_ct == len(self._back):
            # need to make new one bigger by *2 and copy
            self._expand(len(self._back) * 2)

        self._back[self._used_ct] = val
        self._used_ct += 1

    def __str__(self) -> str:
        out_str = ""

        for ix in range(self._used_ct):
            if out_str != "":
                out_str += ", "

            out_str += f"{self._back[ix]}"

        return out_str


if __name__ == "__main__":
    length = 52
    a = LongArrayList(length)
    
    ##
    # quick and dirty checks
    ##
    
    # full backing store is initialized to 0
    for ix in range(length): assert a._back[ix] == 0
    
    # backing store getitem is as we expect
    try:
        a._back[length+1]
    except IndexError:
        pass
    
    # backing storage is right size
    assert len(a._back) == 52
    
    # length of arraylist is qty of used space
    assert len(a) == 0
    a.add(2)
    assert len(a) == 1
    
    # arraylist getitem returns value where it should
    assert 2 == a[0]
    
    # arraylist getitem throws error when there isn't a value at given index
    for k in [-1, 1]:
        try:
            a[k]
        except IndexError:
            pass
    
    # add beyond capacity and observe that the backing storage has changed
    og_size = len(a)
    og_back = a._back
    for ix in range(length): # already added stuff so going to original size will cause expansion
        a.add(ix + 77)
    
    assert og_size + length == len(a)
    
    # is will check identity
    assert (a._back is not og_back)
    
    print(a)
    print("done")

    sys.exit(0)
