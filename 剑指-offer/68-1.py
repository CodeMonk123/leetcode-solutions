# -*- coding: utf-8 -*-
# @Date    : 2021-11-25 16:26:11
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self) -> None:
        self.ans = None
        
    def validate(self, subroot, p, q):
        if self.ans is not None:
            return False, False
        if subroot is None:
            return False, False
        left_contains_p, left_contains_q = self.validate(subroot.left, p, q)
        right_contains_p, right_contains_q = self.validate(subroot.right, p, q)
        contains_p = left_contains_p or right_contains_p or subroot == p
        contains_q = left_contains_q or right_contains_q or subroot == q
        if contains_p and contains_q and self.ans is None:
            self.ans = subroot
        return contains_p, contains_q
        


    def lowestCommonAncestor(self, root, p, q):
        self.validate(root, p, q)
        if self.ans is None:
            return root
        
        return self.ans