# -*- coding: utf-8 -*-

from mdye_misc.linked_list import *


def test_linked_list_node_has_next():
    root = Node(2, Node(45))

    assert root.next_node.val == 45


def test_linked_list_node_has_val():
    root = Node(12)

    assert root.val == 12


def test_linked_list_LinkedList_append():
    lis = LinkedList()

    node22 = Node(22)

    lis.append(node22)

    assert lis.root == node22


def test_linked_list_LinkedList_prepend():
    lis = LinkedList()

    node99 = Node(99)
    node12 = Node(12)

    lis.append(node99)
    lis.prepend(node12)

    assert lis.root == node12
    assert lis.root.next_node == node99


def test_linked_list_LinkedList_search():
    lis = LinkedList()

    lis.append(Node(16)).append(Node(24)).append(Node(99))

    assert lis.search(17) is None
    assert lis.search(24).val == 24


def test_linked_list_gen():
    ct = 300

    node = gen(ct)

    test_ct = 0
    while node is not None:
        assert node.val == test_ct
        test_ct += 1
        node = node.next_node

    assert test_ct == ct


def test_linked_list_gen_in_loop():
    ct = 30000

    node = gen_in_loop(ct)

    test_ct = 0
    while node is not None:
        assert node.val == test_ct
        test_ct += 1
        node = node.next_node

    assert test_ct == ct


def test_linked_list_prepend_gen():
    lis = LinkedList()

    ct = 24
    for i in range(1, ct + 1):
        lis.prepend(Node(i))

    node = lis.root
    test_ct = ct
    while node is not None:
        assert test_ct == node.val
        test_ct -= 1
        node = node.next_node

    assert test_ct == 0


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
