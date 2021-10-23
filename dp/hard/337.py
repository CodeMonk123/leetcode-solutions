# -*- coding: utf-8 -*-
# @Date    : 2021-10-23 16:51:25
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
    def _rob(self, subroot:TreeNode)->Tuple[int,int]:
        if subroot is None:
            return 0, 0
        left_value1, left_value2 = self._rob(subroot.left)
        right_value1, right_value2 = self._rob(subroot.right)
        return subroot.val + left_value2 + right_value2, max(left_value1 + right_value2, left_value1 + right_value1, left_value2 + right_value1, left_value2+right_value2)

    def rob(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self._rob(root))

