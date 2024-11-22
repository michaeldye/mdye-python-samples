"""."""

from typing import Any, List, Optional


# given definition for a Node
class Node:
    def __init__(self, val: Any = None, children: Optional[List["Node"]] = None):
        """."""
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Optional[Node]) -> List[int]:
        """."""
        nodes = []

        def p0(node: Node):
            if not node:
                return

            nodes.append(node.val)

            # a little lame that leetcode doesn't use an empty list for children
            if node is not None and node.children:
                for ch in node.children:
                    p0(ch)

        if not root:
            return []

        p0(root)
        return nodes


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
