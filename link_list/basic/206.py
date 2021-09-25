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
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        p, q = head, head.next
        r = q.next
        p.next = None
        while True:
            q.next = p
            p = q
            q = r
            if r is None:
                break
            r = r.next

        return p


solution = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
print(head)

print(solution.reverseList(head))