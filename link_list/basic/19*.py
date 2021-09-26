class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None:
            return None

        slow, fast = head, head
        dummy_head = ListNode(val=-1, next=head)
        old_slow = dummy_head

        for _ in range(n):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            old_slow = slow
            slow = slow.next

        old_slow.next = slow.next

        return dummy_head.next
