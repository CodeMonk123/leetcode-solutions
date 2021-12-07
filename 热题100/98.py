# -*- coding: utf-8 -*-
# @Date    : 2021-12-06 11:18:37
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
    def isValidBST(self, root: TreeNode) -> bool:
        inorder = []
        s = []
        if root is None:
            return True
        s.append(root)
        p = root.left
        while len(s) != 0:
            while p is not None:
                s.append(p)
                p = p.left
            if len(s) != 0:
                q = s.pop()
                inorder.append(q.val)
                if q.right is not None:
                    s.append(q.right)
                    p = q.right.left
        
        for i in range(1, len(inorder)):
            if inorder[i] < inorder[i-1]:
                return False
        
        return True