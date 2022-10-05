# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_1367 import Solution, ListNode, TreeNode


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_1367_basic(sol: Solution):
    tt = TreeNode(
        1,
        TreeNode(4, right=TreeNode(2, left=TreeNode(1))),
        TreeNode(
            4,
            left=TreeNode(
                2,
                left=TreeNode(6),
                right=TreeNode(8, left=TreeNode(1), right=TreeNode(3)),
            ),
        ),
    )

    assert sol.isSubPath(ListNode(4, ListNode(2, ListNode(8))), tt)

    assert not sol.isSubPath(
        ListNode(1, ListNode(4, ListNode(2, ListNode(6, ListNode(8))))), tt
    )


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
