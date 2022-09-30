# -*- coding: utf-8 -*-

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        max_diff = 0

        def bal0(node: Optional[TreeNode], depth: int) -> int:
            if not node:
                return depth

            left = bal0(node.left, depth + 1)
            right = bal0(node.right, depth + 1)

            nonlocal max_diff

            max_diff = max(abs(right - left), max_diff)
            return max(right, left)

        bal0(root, 0)
        return max_diff <= 1

# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
