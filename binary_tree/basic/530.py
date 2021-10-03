#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self._vals = []

    def _travel(self, subroot: TreeNode):
        if subroot is None:
            return
        self._travel(subroot.left)
        self._vals.append(subroot.val)
        self._travel(subroot.right)

    def getMinimumDifference(self, root: TreeNode) -> int:
        self._travel(root)
        min_difference = self._vals[1] - self._vals[0]
        for i in range(1, len(self._vals)):
            if self._vals[i] - self._vals[i - 1] < min_difference:
                min_difference = self._vals[i] - self._vals[i - 1]

        return min_difference