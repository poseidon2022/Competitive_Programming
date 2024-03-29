# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mine = defaultdict(lambda:0)
        while head!=None:
            mine[head]+=1
            if mine[head]>1:
                return True
            head = head.next
        return False