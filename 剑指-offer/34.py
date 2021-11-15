# -*- coding: utf-8 -*-
# @Date    : 2021-11-15 10:27:49
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
        
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        if root is None:
            return []
        
        if root.left is None and root.right is None:
            if root.val == target:
                return [[root.val]]
            else:
                return []
        else:
            paths = self.pathSum(root.left, target - root.val) + self.pathSum(root.right, target - root.val)
            for path in paths:
                path.insert(0, root.val)
            return paths
        