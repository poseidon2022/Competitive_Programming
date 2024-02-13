# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, end: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        ans = dummy
        c = 0
        prev = None
        while dummy:
            if c==left - 1: bef_sta =dummy
            if c==left: sta = dummy
            if c>left and c<=end:
                nxt = dummy.next
                dummy.next = prev
                prev = dummy
                if c==end: bef_sta.next = dummy
                dummy = nxt
                c+=1
                continue
            if c==end+1: sta.next = dummy
            prev = dummy
            dummy = dummy.next
            c+=1
        
        if c==end+1: sta.next = None
        return ans.next


    
        