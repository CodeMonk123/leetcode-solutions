class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.traversal = []

    def _travel(self, subroot: TreeNode):
        if subroot is None:
            return
        self._travel(subroot.left)
        self.traversal.append(subroot.val)
        self._travel(subroot.right)

    def isValidBST(self, root: TreeNode) -> bool:
        self._travel(root)
        for i in range(1, len(self.traversal)):
            if self.traversal[i] <= self.traversal[i - 1]:
                return False

        return True