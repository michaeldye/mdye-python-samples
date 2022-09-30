# -*- coding: utf-8 -*-

import pytest

from mdye_leetcode.solution_110 import Solution, TreeNode


# makes a Solution object b/c that's how leetcode rolls
@pytest.fixture(scope="module")
def sol():
    yield Solution()


def test_solution_110_basic(sol: Solution):
    assert sol.isBalanced(TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))))
    assert not sol.isBalanced(TreeNode(1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4), right=TreeNode(4)), right=TreeNode(3)), right=TreeNode(2)))



# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
