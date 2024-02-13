# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        s,f = head, head
        for_lat = head
        c = False
        while f and f.next:
            f = f.next.next
            s = s.next
            if f==s:
                c = not c 
                break
            
        if not c: return None

        while for_lat:
            if f==for_lat: return f
            for_lat = for_lat.next
            f = f.next
        

        

        