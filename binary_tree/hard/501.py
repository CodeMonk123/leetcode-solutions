from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self._vals = []

    def _inorder_travel(self, subroot: TreeNode):

        if subroot is None:
            return
        self._inorder_travel(subroot.left)
        self._vals.append(subroot.val)
        self._inorder_travel(subroot.right)

    def findMode(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        self._inorder_travel(root)
        modes = [self._vals[0]]
        max_count = 1
        count = 1
        current_val = self._vals[0]
        for i in range(1, len(self._vals)):
            if self._vals[i] == current_val:
                count += 1
                if count == max_count:
                    modes.append(current_val)
                if count > max_count:
                    modes = [current_val]
                    max_count = count
            else:
                count = 1
                current_val = self._vals[i]
                if count == max_count:
                    modes.append(current_val)
        return modes