from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _generate_paths(self, subroot: TreeNode) -> List[str]:
        if subroot is None:
            return ['']

        if subroot.left is None and subroot.right is None:
            return [str(subroot.val)]

        paths = []

        if subroot.left is not None:
            left_paths = self._generate_paths(subroot.left)
            for path in left_paths:
                paths.append('{}->'.format(subroot.val) + path)

        if subroot.right is not None:
            right_paths = self._generate_paths(subroot.right)
            for path in right_paths:
                paths.append('{}->'.format(subroot.val) + path)

        return paths

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        return self._generate_paths(root)