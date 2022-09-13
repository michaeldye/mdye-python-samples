#!/usr/bin/env python3

## linked list
#
# append: O(N) , appending 1 item requires we traverse whole list to get to end
# prepend: O(1) , prepending just needs a few values set (references rearranged)
# search: O(N) worst case, avg. case O(N) still? best case is O(1)

# good for: cases when you can use prepend for adding, you get guaranteed constant
# time without any pauses for arraylist expansion, say

import sys
from typing import Any, Optional


class Node(object):
    _next = None
    _value = None

    def __init__(self, vv: int, nn: "Node" = None):

        self._next = nn
        self._value = vv

    @property
    def val(self) -> Any:
        return self._value

    @property
    def next_node(self) -> "Node":
        return self._next

    @next_node.setter
    def next_node(self, node: "Node") -> None:
        self._next = node

    def __str__(self) -> str:
        return f"value: {self.val}"


class LinkedList(object):
    root = None

    def __init__(self):
        # can make an empty one
        pass

    def append(self, to_add: Node) -> "LinkedList":

        if self.root is None:
            self.root = to_add
        else:
            last = self.root
            while True:
                if last.next_node is None:
                    # now last really is end of list; iterated through all nodes to get here
                    break
                last = last.next_node

            last.next_node = to_add

        return self

    def prepend(self, to_add: Node) -> "LinkedList":
        to_add.next_node = self.root
        self.root = to_add

        return self

    def search(self, val: Any) -> Optional[Any]:
        n = self.root

        while n is not None:
            if n.val == val:
                return val
            n = n._next

        return None

    def __str__(self) -> str:
        out_str = ""

        nn = self.root
        while True:
            if nn is None:
                break
            elif nn != self.root:
                out_str += ", "

            out_str += f"{nn}"
            nn = nn.next_node

        return out_str


def print_nodes(node: Node) -> None:
    while node is not None:
        print(node)
        node = node.next_node


def gen_in_loop(ct: int) -> Node:
    # will return the root node (with value 0); this was the last node to be created

    next_n = None
    for ix in range(ct):
        # don't want 1 ... 24 so we subtract 1 from ct when deciding the value
        value = ct - ix - 1
        next_n = Node(value, next_n)

    return next_n


def gen(ct: int) -> Node:
    # will return the root node (with value 0); this was the last node to get created

    def gen0(n: int) -> Node:

        if n == ct:
            return None
        return Node(n, gen0(n + 1))

    return gen0(0)


if __name__ == "__main__":
    print("List of Nodes generated in loop")
    print_nodes(gen_in_loop(24))

    print("List of Nodes generated recursively")
    print_nodes(gen(24))

    print("List generated with LinkedList append: * really slow!! *")
    la = LinkedList()
    for i in range(24):
        la.append(Node(i))

    print("LinkedList filled using append")
    print(la)

    lp = LinkedList()
    ct = 24
    for i in range(ct):
        lp.prepend(Node(ct - 1 - i))

    print("LinkedList filled using prepend: plenty fast")
    print(lp)

    # search for a given node
    assert lp.search(22)
    assert not lp.search(2000)

    print("done")
    sys.exit(0)
