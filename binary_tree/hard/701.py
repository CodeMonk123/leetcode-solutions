# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _insert(self, subroot: TreeNode, val: int):
        if subroot.val > val:
            if subroot.left is None:
                subroot.left = TreeNode(val=val)
            else:
                self._insert(subroot=subroot.left, val=val)
        else:
            if subroot.right is None:
                subroot.right = TreeNode(val=val)
            else:
                self._insert(subroot=subroot.right, val=val)

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val=val)

        self._insert(root, val)

        return root