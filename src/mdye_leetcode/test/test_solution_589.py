# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_589 import Solution, Node


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_589_basic(sol: Solution):
    root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])

    assert sol.preorder(root) == [1, 3, 5, 6, 2, 4]


def test_solution_589_empty_input(sol: Solution):
    assert sol.preorder(None) == []


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
