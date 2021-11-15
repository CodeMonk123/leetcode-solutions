# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        new_head = ListNode(-1)
        r = new_head
        p,q = l1, l2
        while p is not None and q is not None:
            if p.val < q.val:
                new_node = ListNode(p.val)
                r.next = new_node
                r = r.next
                p = p.next
            else:
                new_node = ListNode(q.val)
                r.next = new_node
                r = r.next
                q = q.next
        
        if p is None:
            while q is not None:
                new_node = ListNode(q.val)
                r.next = new_node
                r = r.next
                q = q.next

        if q is None:
            while p is not None:
                new_node = ListNode(p.val)
                r.next = new_node
                r = r.next
                p = p.next
        
        return new_head.next