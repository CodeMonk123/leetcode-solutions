# -*- coding: utf-8 -*-
# @Date    : 2021-11-22 15:56:56
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        q = []
        res = []
        q = [root]
        while len(q) > 0:
            p = q.pop(0)
            if p is not None:
                res.append(p.val)
                q.append(p.left)
                q.append(p.right)
        
        return res