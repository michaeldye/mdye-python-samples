# -*- coding: utf-8 -*-

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True

        if not root:
            return False

        if head.val == root.val:
            rest = head.next
        else:
            rest = head

        return self.isSubPath(rest, root.left) or self.isSubPath(rest, root.right)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
