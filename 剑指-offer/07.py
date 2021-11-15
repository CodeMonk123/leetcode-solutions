# -*- coding: utf-8 -*-
# @Date    : 2021-11-10 10:19:43
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        
        if len(preorder) == 1:
            return TreeNode(preorder[0])
        
        root_val = preorder[0]
        root = TreeNode(root_val)
        left_count = 0
        for i in range(len(inorder)):
            if inorder[i] == root_val:
                break
            else:
                left_count += 1
        
        root.left = self.buildTree(preorder[1:1+left_count], inorder[:left_count])
        root.right = self.buildTree(preorder[1+left_count:], inorder[1+left_count:])
        return root
