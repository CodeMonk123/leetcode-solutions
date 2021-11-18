# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 16:47:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self) -> None:
        self.ans = None

    def _search(self, subroot:TreeNode, p:TreeNode, q:TreeNode):
        if self.ans is not None:
            return False, False
        if subroot is None:
            return False, False
        else:
            left_contains_p, left_contains_q = self._search(subroot.left, p, q)
            right_contains_p, right_contains_q = self._search(subroot.right, p, q)
            if left_contains_p and left_contains_q or right_contains_p and right_contains_q:
                return False, False
            else:
                contains_p = left_contains_p or right_contains_p or subroot.val == p.val
                contains_q = left_contains_q or right_contains_q or subroot.val == q.val
                if contains_p and contains_q:
                    self.ans = subroot
                return contains_p, contains_q
        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ans = None
        self._search(root, p, q)
        return self.ans