class ListNode:
    def __init__(self, val = -1, next = None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.count = 0

    def get(self, index: int) -> int:
        cur = 0
        head2 = self.head
        while head2:
            if cur==index: return head2.val
            head2 = head2.next
            cur+=1
        return -1
    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val)
        if self.count: new_head.next = self.head
        else: new_head.next = None
        self.head = new_head
        self.count+=1
    def addAtTail(self, val: int) -> None:
        self.count+=1
        added = ListNode(val)
        head2 = self.head
        if self.head.val==-1:
            self.head.next = added
            self.head = self.head.next
            return
        while self.head:
            if not self.head.next:
                self.head.next = added
                self.head = self.head.next
                break
            self.head = self.head.next

        self.head = head2

    def addAtIndex(self, index: int, val: int) -> None:
        added = ListNode(val)
        head2 = self.head
        cur = 0

        if index==0:
            self.addAtHead(val)
            return
        while self.head:
            if cur == index - 1:
                added.next = self.head.next
                self.head.next = added
                break 
            self.head = self.head.next
            cur+=1
        
        self.head = head2

    def deleteAtIndex(self, index: int) -> None:

        cur = 0
        head2 = self.head
        if index==0:
            self.head = self.head.next
            return
        while self.head.next:
            if cur == index - 1:
                self.head.next = self.head.next.next
                break
            cur+=1
            self.head = self.head.next
        
        self.head = head2


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)