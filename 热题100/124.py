# -*- coding: utf-8 -*-
# @Date    : 2021-12-08 10:10:21
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple, Optional
import copy

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        self.max_path_sum = -1000

    def _max_path_sum(self, subroot:TreeNode)->int:
        if subroot.left is None and subroot.right is None:
            path1 = subroot.val
            path2 = subroot.val
            if path1 > self.max_path_sum:
                self.max_path_sum = path1
            return max(0, path2)
        elif subroot.left is None:
            right_path2 = self._max_path_sum(subroot.right)
            path1 = subroot.val + right_path2
            if path1 > self.max_path_sum:
                self.max_path_sum = path1
            return max(0, path1)
        elif subroot.right is None:
            left_path2 = self._max_path_sum(subroot.left)
            path1 = subroot.val + left_path2
            if path1 > self.max_path_sum:
                self.max_path_sum = path1
            return max(0, path1)
        else:
            right_path2 = self._max_path_sum(subroot.right)
            left_path2 = self._max_path_sum(subroot.left)
            path1 = subroot.val + right_path2 + left_path2
            if path1 > self.max_path_sum:
                self.max_path_sum = path1
            path2 = max(0, subroot.val + right_path2, subroot.val + left_path2)
            return path2


        

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self._max_path_sum(root)
        return self.max_path_sum