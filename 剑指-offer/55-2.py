# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 15:36:47
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
    def _depth(self, subroot:TreeNode):
        if subroot is None:
            return 0, True
        left_depth, left_balanced = self._depth(subroot.left)
        right_depth, right_balanced = self._depth(subroot.right)
        depth = 1 + max(left_depth, right_depth)
        if abs(left_depth-right_depth) > 1:
            return depth, False
        return depth, left_balanced and right_balanced

    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left_depth, left_balanced = self._depth(root.left)
        right_depth, right_balanced = self._depth(root.right)
        if abs(left_depth-right_depth) > 1:
            return False

        return left_balanced and right_balanced      