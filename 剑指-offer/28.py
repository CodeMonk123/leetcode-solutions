# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 11:05:16
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
    def _is_symmetric(self, subroot1:TreeNode, subroot2: TreeNode)->bool:
        if subroot1 is None and subroot2 is None:
            return True
        elif subroot1 is None:
            return False
        elif subroot2 is None:
            return False
        
        if subroot1.val != subroot2.val:
            return False
        
        return self._is_symmetric(subroot1.left, subroot2.right) and self._is_symmetric(subroot1.right, subroot2.left)
        

    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return self._is_symmetric(root.left, root.right)