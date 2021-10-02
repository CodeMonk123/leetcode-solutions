from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        max_val = max(nums)
        max_index = nums.index(max_val)
        subroot = TreeNode(max_val)
        subroot.left = self.constructMaximumBinaryTree(nums[:max_index])
        subroot.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return subroot
