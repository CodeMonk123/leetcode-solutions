# -*- coding: utf-8 -*-
# @Date    : 2021-12-07 10:07:59
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        q = [root]
        next_q = []
        vals = []
        while True:
            while len(q) != 0:
                node = q.pop(0)
                vals.append(node.val)
                if node.left is not None:
                    next_q.append(node.left)
                if node.right is not None:
                    next_q.append(node.right)
            res.append(vals)
            vals = []
            if len(next_q) == 0:
                break
            q = next_q
            next_q = []
        return res
