class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.left_leaves_sum = 0

    def _sum(self, subroot: TreeNode, is_left: bool):
        if subroot is None:
            return

        if subroot.left is None and subroot.right is None and is_left:
            self.left_leaves_sum += subroot.val

        self._sum(subroot.left, True)
        self._sum(subroot.right, False)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.left_leaves_sum = 0
        self._sum(root, False)
        return self.left_leaves_sum