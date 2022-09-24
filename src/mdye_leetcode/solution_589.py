# -*- coding: utf-8 -*-

from typing import List

# given definition for a Node
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: "Node") -> List[int]:
        nodes = []

        def p0(node: "Node"):
            if not node:
                return

            nodes.append(node.val)

            # kinda lame that they don't initialize children with an empty list
            if node.children is not None:
                for ch in node.children:
                    p0(ch)

        p0(root)
        return nodes


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4
