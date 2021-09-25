# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if self.next is None:
            return ''
        return '{}->{}'.format(self.val, self.next)


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(val=-1, next=head)
        p, q = new_head, head
        while q is not None:
            if q.val == val:
                p.next = q.next
                q = q.next
            else:
                p = q
                q = q.next

        return new_head.next
