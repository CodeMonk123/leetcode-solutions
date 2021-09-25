# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if self.next is None:
            return '{}'.format(self.val)
        return '{}->{}'.format(self.val, self.next)


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p, q = head, head.next
        r = q.next
        new_head = q
        old_p = p
        while True:
            q.next = p
            if r is None or r.next is None:
                p.next = r
                break
            p.next = r.next
            p, q = r, r.next
            r = q.next

        return new_head


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(head)

print(solution.swapPairs(head))