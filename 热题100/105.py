# Definition for a binary tree node.
class Solution:
    def _build(self, preorder:List[int], inorder:List[int], start1:int, end1:int, start2:int, end2:int)->TreeNode:
        if start1 == end1:
            return TreeNode(val=preorder[start1])
        elif start1 > end1:
            return None
        
        subroot = TreeNode(val=preorder[start1])
        left_count = 0
        for i in range(start2, end2+1):
            if inorder[i] == preorder[start1]:
                break
            left_count += 1
        subroot.left = self._build(preorder, inorder, start1+1, start1+left_count, start2, start2 + left_count -1)
        subroot.right = self._build(preorder, inorder, start1 + left_count + 1, end1, start2 + left_count + 1, end2)
        return subroot


    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        n = len(preorder)
        if n == 0:
            return None

        return self._build(preorder, inorder, 0, n-1, 0, n-1)    