# -*- coding: utf-8 -*-
# @Date    : 2021-11-04 15:42:28
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
        self.values = []
        
    
    def pre_order(self, subroot:TreeNode):
        if subroot is None:
            return
        
        self.pre_order(subroot.left)
        self.values.append(subroot.val)
        self.pre_order(subroot.right)


    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.values = []
        self.k = k
        self.pre_order(root)
        return self.values[-k]