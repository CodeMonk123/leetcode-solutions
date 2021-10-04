from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _build_bst(self, nums: List[int], start: int, end: int) -> TreeNode:
        if start > end:
            return None
        if start == end:
            return TreeNode(val=nums[start])
        mid = int((start + end) / 2)
        subroot = TreeNode(val=nums[mid])
        subroot.left = self._build_bst(nums, start, mid - 1)
        subroot.right = self._build_bst(nums, mid + 1, end)
        return subroot

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._build_bst(nums, 0, len(nums) - 1)