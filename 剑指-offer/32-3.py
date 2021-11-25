# -*- coding: utf-8 -*-
# @Date    : 2021-11-22 16:56:57
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
        left_to_right = True
        while len(current_layer) > 0:
            temp = []
            next_layer = []
            if left_to_right:
                for node in current_layer:
                    if node is not None:
                        temp.append(node.val)
                        next_layer.append(node.left)
                        next_layer.append(node.right)
            else:
                for i in range(len(current_layer)-1, -1, -1):
                    node = current_layer[i]
                    if node is not None:
                        temp.append(node.val)
                        next_layer.append(node.right)
                        next_layer.append(node.left)
                next_layer.reverse()
            current_layer = next_layer
            left_to_right = not left_to_right
            if len(temp) > 0:
                res.append(temp)
        return res