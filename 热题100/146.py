# -*- coding: utf-8 -*-
# @Date    : 2021-12-09 10:15:20
# @Author  : CodeMonk123

from typing import List
from typing import Dict, Tuple
import copy

class LRUCache:
    class ListNode:
        def __init__(self, key:int, val:int) -> None:
            self.key = key
            self.val = val
            self.next:LRUCache.ListNode = None
            self.pre:LRUCache.ListNode = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LRUCache.ListNode(-1,-1)
        self.tail = None
        self.key_to_node:Dict[int, LRUCache.ListNode] = {}


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        target_node = self.key_to_node[key]
        res = target_node.val
        if target_node != self.tail:
            target_node.pre.next = target_node.next
            target_node.next.pre = target_node.pre
            self.tail.next = target_node
            target_node.pre = self.tail
            target_node.next = None
            self.tail = target_node
        
        return res
        


    def put(self, key: int, value: int) -> None:
        if key not in self.key_to_node:
            if len(self.key_to_node) == 0:
                # first element
                node = LRUCache.ListNode(key=key,val=value)
                self.head.next = node
                node.pre = self.head
                self.tail = node
                self.key_to_node[key] = node
            elif len(self.key_to_node) == self.capacity:
                node = LRUCache.ListNode(key=key,val=value)
                remove_node = self.head.next
                if self.tail == remove_node:
                    self.tail = None
                new_first_node = self.head.next.next
                self.head.next = new_first_node
                if new_first_node is not None:
                    new_first_node.pre = self.head
                self.key_to_node.pop(remove_node.key)
                if self.tail is None:
                    node = LRUCache.ListNode(key=key,val=value)
                    self.head.next = node
                    node.pre = self.head
                    self.tail = node
                    self.key_to_node[key] = node
                else:
                    node = LRUCache.ListNode(key=key,val=value)
                    self.tail.next = node
                    node.pre = self.tail
                    self.tail = node
                    self.key_to_node[key] = node
            else:
                node = LRUCache.ListNode(key=key,val=value)
                self.tail.next = node
                node.pre = self.tail
                self.tail = node
                self.key_to_node[key] = node
        else:
            target_node = self.key_to_node[key]
            target_node.val = value
            if target_node != self.tail:
                target_node.pre.next = target_node.next
                target_node.next.pre = target_node.pre
                self.tail.next = target_node
                target_node.pre = self.tail
                target_node.next = None
                self.tail = target_node







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)