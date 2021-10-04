from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _delete(self, subroot: Optional[TreeNode],
                key: int) -> Optional[TreeNode]:
        if subroot is None:
            return None

        if subroot.val == key:
            if subroot.left is None and subroot.right is None:
                return None
            elif subroot.left is None:
                return subroot.right
            elif subroot.right is None:
                return subroot.left
            else:
                p = subroot.right
                while p.left is not None:
                    p = p.left
                p.left = subroot.left
                return subroot.right

        elif subroot.val > key:
            subroot.left = self._delete(subroot.left, key)
        else:
            subroot.right = self._delete(subroot.right, key)

        return subroot

    def deleteNode(self, root: Optional[TreeNode],
                   key: int) -> Optional[TreeNode]:

        new_root = self._delete(root, key)
        return new_root