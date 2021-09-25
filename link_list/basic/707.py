class MyNode:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None
        self.tail = None
        self.dummy_head = MyNode(val=-1, next=self.head)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length:
            return -1
        p: MyNode = self.head
        for _ in range(index):
            p = p.next
        return p.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = MyNode(val=val, next=self.head)
        self.dummy_head.next = new_head
        self.head = new_head
        if self.tail is None:
            self.tail = self.head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_tail = MyNode(val=val)
        if self.tail is None:
            self.head = new_tail
            self.tail = new_tail
            self.dummy_head.next = new_tail
            self.length += 1
            return
        self.tail.next = new_tail
        self.tail = new_tail
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.length or index < 0:
            return

        new_node = MyNode(val=val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.dummy_head.next = new_node
            self.length += 1
            return

        q: MyNode = self.dummy_head
        p: MyNode = self.head
        for _ in range(index):
            q = q.next
            p = p.next
        new_node.next = p
        q.next = new_node
        if index == self.length:
            self.tail = new_node
        if index == 0:
            self.head = new_node

        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.length or index < 0:
            return

        q: MyNode = self.dummy_head
        p: MyNode = self.head
        for _ in range(index):
            q = q.next
            p = p.next
        q.next = p.next
        self.length -= 1
        if index == 0:
            self.head = self.dummy_head.next
            if self.length == 0:
                self.tail = None

        if index == self.length:
            self.tail = q
