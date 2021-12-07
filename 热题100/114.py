# -*- coding: utf-8 -*-
# @Date    : 2021-12-07 10:35:12
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def _flatten(self, subroot: TreeNode)->TreeNode:
        """ flatten tree and return tail node """
        if subroot.left is None and subroot.right is None:
            return subroot
        elif subroot.left is None:
            right_tail = self._flatten(subroot.right)
            return right_tail
        elif subroot.right is None:
            left_tail = self._flatten(subroot.left)
            subroot.right = subroot.left
            subroot.left = None
            return left_tail
        else:
            left_tail = self._flatten(subroot.left)
            right_tail = self._flatten(subroot.right)
            left_tail.right = subroot.right
            subroot.right = subroot.left
            subroot.left = None
            return right_tail

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        
        self._flatten(root)