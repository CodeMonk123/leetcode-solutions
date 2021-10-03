from typing import Tuple


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self) -> None:
        self._lowest_ancestor = None

    def _inorder_travel(self, subroot, p, q) -> Tuple[bool, bool]:
        if subroot is None:
            return False, False

        is_p_ancestor = False
        is_q_ancestor = False

        left_is_p_ancestor, left_is_q_ancestor = self._inorder_travel(
            subroot.left, p, q)
        right_is_p_ancestor, right_is_q_ancestor = self._inorder_travel(
            subroot.right, p, q)

        is_p_ancestor = left_is_p_ancestor or right_is_p_ancestor or subroot == p
        is_q_ancestor = right_is_q_ancestor or left_is_q_ancestor or subroot == q

        if is_p_ancestor and is_q_ancestor:
            if self._lowest_ancestor is None:
                self._lowest_ancestor = subroot
        return is_p_ancestor, is_q_ancestor

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode',
                             q: 'TreeNode') -> 'TreeNode':
        self._lowest_ancestor = None
        self._inorder_travel(root, p, q)
        return self._lowest_ancestor