# -*- coding: utf-8 -*-
# @Date    : 2021-12-06 10:30:38
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
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s = []
        res = []
        if root is None:
            return []
        s.append((root, 'L'))
        p = root.left
        while len(s) != 0:
            while p is not None:
                s.append((p, 'L'))
                p = p.left
            if len(s) != 0:
                sub_root, sign = s.pop()
                if sign == 'L':
                    res.append(sub_root.val)
                    s.append((sub_root, 'R'))
                    p = sub_root.right
                else:
                    pass
        return res

solution = Solution()
root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))        
print(solution.inorderTraversal(root))
        
