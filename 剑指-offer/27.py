# -*- coding: utf-8 -*-
# @Date    : 2021-11-18 11:25:18
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
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return None
        mirrored_root = TreeNode(root.val)
        mirrored_root.left = self.mirrorTree(root.right)
        mirrored_root.right = self.mirrorTree(root.left)
        return mirrored_root