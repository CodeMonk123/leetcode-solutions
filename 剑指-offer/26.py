# -*- coding: utf-8 -*-
# @Date    : 2021-11-05 09:55:37
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
    def is_equal(self, subroot1: TreeNode, subroot2: TreeNode) -> bool:
        if subroot1 is None and subroot2 is None:
            return True
        elif subroot1 is None:
            return False
        elif subroot2 is None:
            return True
        else:
            if subroot1.val != subroot2.val:
                return False
            else:
                return self.is_equal(subroot1.left, subroot2.left) and self.is_equal(subroot1.right, subroot2.right)


    def find(self, subroot_A: TreeNode, B:TreeNode) -> bool:
        if subroot_A is None:
            return False
        
        if subroot_A.val == B.val:
            return self.is_equal(subroot_A, B) or self.find(subroot_A.left, B) or self.find(subroot_A.right, B)
        else:
            return self.find(subroot_A.left, B) or self.find(subroot_A.right, B)
           

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False
        
        return self.find(A, B)
        
