from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: Node) -> List[int]:
        ans = []
        st: List[Node] = []
        if root is not None:
            st.append(root)
            while len(st) != 0:
                subroot = st.pop()
                ans.append(subroot.val)
                for i in range(len(subroot.children) - 1, -1, step=-1):
                    st.append(subroot.children[i])

        return ans