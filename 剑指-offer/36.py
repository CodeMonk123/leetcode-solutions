# -*- coding: utf-8 -*-
# @Date    : 2021-11-10 11:03:27
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def build_list(self, subroot):
        if subroot.left is None and subroot.right is None:
            return 
        
        if subroot.left is not None:
            p = subroot.left
            while p.right is not None:
                p = p.right
            
            self.build_list(subroot.left)
            p.right = subroot
            subroot.left = p
        
        if subroot.right is not None:
            p = subroot.right
            while p.left is not None:
                p = p.left
            self.build_list(subroot.right)
            p.left = subroot
            subroot.right = p



    def treeToDoublyList(self, root) :
        if root is None:
            return None
        p = root
        while p.left is not None:
            p = p.left
        head = p

        p = root
        while p.right is not None:
            p = p.right
        tail = p
        
        self.build_list(root)
        head.left = tail
        tail.right = head
        return head