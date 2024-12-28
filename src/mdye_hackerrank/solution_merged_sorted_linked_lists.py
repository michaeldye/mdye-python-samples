"""."""

import os
from typing import Optional


class SinglyLinkedListNode:
    def __init__(self, node_data):  # noqa: ANN001, D107
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):  # noqa: D107
        self.head = None
        self.tail = None

    def insert_node(self, node_data):  # noqa: ANN001, ANN201, D102
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node  # type: ignore

        self.tail = node


def print_singly_linked_list(node, sep, fptr):  # noqa: ANN001, ANN201, D103
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the mergeLists function below.


#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(  # noqa: D103, N802
    head1: SinglyLinkedListNode, head2: SinglyLinkedListNode
) -> Optional[SinglyLinkedListNode]:
    merged = SinglyLinkedList()

    h1 = head1
    h2 = head2

    # more space efficient than a heap but that's an ideal ds for this problem
    while True:
        if h1 is None:
            if h2 is None:
                break
            else:
                # h2 is not None but h1 is, add h2 and continue
                merged.insert_node(h2.data)
                h2 = h2.next
        else:
            # h1 is not None
            if h2 is None:
                merged.insert_node(h1.data)
                h1 = h1.next
            else:
                # h1 and h2 are both not None, compare and push least; leave most for next iteration
                if h1.data < h2.data:
                    d = h1.data
                    h1 = h1.next
                else:
                    d = h2.data
                    h2 = h2.next
                merged.insert_node(d)

    return merged.head  # type: ignore


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")  # noqa: SIM115

    tests = int(input())

    for _ in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        llist3 = mergeLists(llist1.head, llist2.head)  # type: ignore

        print_singly_linked_list(llist3, " ", fptr)
        fptr.write("\n")

    fptr.close()


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
