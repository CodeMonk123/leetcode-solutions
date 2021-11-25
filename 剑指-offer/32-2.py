# -*- coding: utf-8 -*-
# @Date    : 2021-11-22 16:00:00
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        current_layer = [root]
        next_layer = []
        while len(current_layer) > 0:
            temp = []
            for node in current_layer:
                if node is not None:
                    temp.append(node.val)
                    next_layer.append(node.left)
                    next_layer.append(node.right)
            if len(temp) > 0:
                res.append(temp)
            current_layer = next_layer
            next_layer = []
        return res
            

    