from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root_val = postorder[-1]
        root_idx = inorder.index(root_val)
        sub_root = TreeNode(root_val)
        left_root = self.buildTree(inorder[:root_idx], postorder[:root_idx])
        right_root = self.buildTree(inorder[root_idx + 1:],
                                    postorder[root_idx:-1])
        sub_root.left = left_root
        sub_root.right = right_root
        return sub_root
