class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _min_depth(self, subroot: TreeNode) -> int:
        if subroot is None:
            return 1e8

        if subroot.left is None and subroot.right is None:
            return 1

        return 1 + min(self._min_depth(subroot.left),
                       self._min_depth(subroot.right))

    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0

        return self._min_depth(root)