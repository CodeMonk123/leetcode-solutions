from typing import List, Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _sum(self, subroot: TreeNode, target: int) -> Set[int]:
        if subroot is None:
            return set()

        if subroot.left is None and subroot.right is None:
            return set([subroot.val])

        sums = self._sum(subroot.left,
                         target).union(self._sum(subroot.right, target))
        sums = set(map(lambda x: x + subroot.val, sums))
        return sums

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        sums = self._sum(root, targetSum)
        return targetSum in sums