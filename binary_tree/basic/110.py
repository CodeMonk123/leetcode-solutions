from typing import Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _depth(self, subroot: TreeNode) -> Tuple[int, bool]:
        if subroot is None:
            return 0, True
        elif subroot.right is None and subroot.left is None:
            return 1, True
        else:
            left_depth, left_balanced = self._depth(subroot.left)
            right_depth, right_balanced = self._depth(subroot.right)
            if not left_balanced or not right_balanced:
                return -1, False
            elif abs(left_depth - right_depth) <= 1:
                return 1 + max(left_depth, right_depth), True
            else:
                return -1, False

    def isBalanced(self, root: TreeNode) -> bool:
        _, balanced = self._depth(root)
        return balanced