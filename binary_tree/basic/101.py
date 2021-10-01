# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True

        layer_size = 1
        q = [root]
        while len(q) != 0:
            s = []
            count = 0
            for i in range(layer_size):
                subroot = q.pop(0)
                if subroot.left is not None:
                    count += 1
                    q.append(subroot.left)
                if subroot.right is not None:
                    count += 1
                    q.append(subroot.right)
                s.append(subroot.left)
                s.append(subroot.right)

            i, j = 0, len(s) - 1
            while i < j:
                if s[i] is None and s[j] is not None or s[i] is not None and s[
                        j] is None or s[i] is not None and s[
                            j] is not None and s[i].val != s[j].val:
                    return False
                i += 1
                j -= 1

            layer_size = count

        return True
