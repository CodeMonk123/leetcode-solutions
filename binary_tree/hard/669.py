class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    def _trim(self, subroot: TreeNode, low: int, high: int) -> TreeNode:
        if subroot is None:
            return None

        if subroot.val < low:
            return self._trim(subroot.right, low, high)
        elif subroot.val > high:
            return self._trim(subroot.left, low, high)
        else:
            subroot.left = self._trim(subroot.left, low, high)
            subroot.right = self._trim(subroot.right, low, high)
            return subroot

    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        new_root = self._trim(root, low, high)
        return new_root