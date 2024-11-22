"""."""

from typing import Optional


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ):
        """."""
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time complexity b/c we visit each node only once O(n) space
    # complexity b/c we could recur such that we store n stack frames at once
    #
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """."""

        def bal0(node: Optional[TreeNode], depth: int, max_diff: int) -> tuple[int, int]:
            if not node:
                return depth, max_diff

            left, max_diff = bal0(node.left, depth + 1, max_diff)
            right, max_diff = bal0(node.right, depth + 1, max_diff)

            diff = abs(right - left)

            # return (greater_depth_between_left_and_right, max_depth_diff_found_so_far)
            #
            # max_diff is the highest diff value we've computed so far, we take
            # the greater of that or the diff between this left and right
            # subtree

            return max(right, left), max(diff, max_diff)

        _, max_diff = bal0(root, 0, 0)
        return max_diff <= 1


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
