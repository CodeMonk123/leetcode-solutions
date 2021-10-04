from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def __init__(self) -> None:
    #     self.vals = []
    #     self.val_index = {}
    #     self.sums = []

    # def _inorder_travel(self, subroot: Optional[TreeNode]):
    #     if subroot is None:
    #         return
    #     self._inorder_travel(subroot.left)
    #     self.vals.append(subroot.val)
    #     self._inorder_travel(subroot.right)

    # def _convert(self, subroot: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if subroot is None:
    #         return None
    #     new_subroot = TreeNode(val=self.sums[self.val_index[subroot.val]])
    #     new_subroot.left = self._convert(subroot.left)
    #     new_subroot.right = self._convert(subroot.right)
    #     return new_subroot

    # def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     self.vals = []
    #     self._inorder_travel(root)
    #     val_sum = 0
    #     total_sum = sum(self.vals)
    #     for index, val in enumerate(self.vals):
    #         val_sum += val
    #         self.val_index[val] = index
    #         self.sums.append(total_sum - val_sum + val)

    #     return self._convert(root)

    def __init__(self) -> None:
        self.sum = 0

    def _reverse_inorder_travel(self, subroot: Optional[TreeNode]):
        if subroot is None:
            return
        self._reverse_inorder_travel(subroot.right)
        self.sum += subroot.val
        subroot.val = self.sum
        self._reverse_inorder_travel(subroot.left)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        self._reverse_inorder_travel(root)
        return root