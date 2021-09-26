class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None

        slow, fast = head, head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if slow == fast:
                break

        if fast is None:
            return None

        p = head
        q = slow

        while p != q:
            p = p.next
            q = q.next

        return p
