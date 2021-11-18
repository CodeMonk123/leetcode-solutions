# -*- coding: utf-8 -*-
# @Date    : 2021-11-17 11:38:03
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def _encode(self, subroot):
        if subroot is None:
            return 'X'
        else:
            return '({}){}({})'.format(self._encode(subroot.left), subroot.val, self._encode(subroot.right))


    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self._encode(root)

    
    def _decode(self, data:str):
        if data == 'X':
            return None
        
        if not data.startswith('('):
            return TreeNode(int(data))

        left = 1
        index = 0
        for i in range(1, len(data)):
            if data[i] == ')':
                left -= 1
            elif data[i] == '(':
                left += 1
            if left == 0:
                index = i
                break

        end = index+1
        for i in range(index+1, len(data)):
            if data[i] == '(':
                end = i
                break
        
        subroot = TreeNode(int(data[index+1:end]))
        subroot.left = self._decode(data[1:index])
        subroot.right = self._decode(data[end+1:-1])
        return subroot
        



    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self._decode(data)


tree = TreeNode(3)
tree.left = TreeNode(2)
tree.right = TreeNode(4)
tree.left.left = TreeNode(3)

s = Codec()
s.deserialize(s.serialize(tree))