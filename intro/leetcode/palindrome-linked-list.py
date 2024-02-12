# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        new = ListNode(head.val)
        dummy = new
        head2 = head

        while head.next:
            new.next = ListNode(head.next.val) 
            head = head.next
            new = new.next

        prev = None
        while head2:
            nxt = head2.next
            head2.next = prev
            prev = head2
            if not nxt: break
            head2 = nxt
        
        while head:
            if head.val != dummy.val: return False
            dummy = dummy.next
            head = head.next
        
        return True 
