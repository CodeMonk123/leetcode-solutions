# -*- coding: utf-8 -*-
# @Date    : 2021-12-07 10:05:16
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
    def validate(self, left:TreeNode, right:TreeNode)->bool:
        if left is None and right is None:
            return True
        elif left is not None and right is not None:
            if left.val != right.val:
                return False
            return self.validate(left.left, right.right) and self.validate(left.right, right.left)
        else:
            return False

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        return self.validate(root.left, root.right)        