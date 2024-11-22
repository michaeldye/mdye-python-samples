"""."""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        """."""
        self.val = val
        self.next = next_node

    def __str__(self) -> str:
        return f"{self.val=}, {self.next=}"


class TreeNode:
    def __init__(
        self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None
    ):
        """."""
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"{self.val=}, {self.left=}, {self.right=}"


class Solution:
    def is_sub_path(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        """."""

        def dfs(list_n: Optional[ListNode], n: Optional[TreeNode]) -> bool:
            if list_n is None:
                return True

            if n is None:
                return False

            return list_n.val == n.val and (dfs(list_n.next, n.left) or dfs(list_n.next, n.right))

        if head is None:
            return True

        if root is None:
            return False

        # At each node, do depth-first-search attempting to match each node in
        # the list; if no match is found, recur down each branch of the tree
        return (
            dfs(head, root)
            or self.is_sub_path(head, root.left)
            or self.is_sub_path(head, root.right)
        )


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
