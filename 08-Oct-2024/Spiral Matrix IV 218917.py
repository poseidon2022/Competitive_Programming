# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        ans = [[-1 for __ in range(n)] for _ in range(m)]
        r_s, c_s, r_e, c_e = 1, 0, m-1, n-1
        r, d, l, u = True, False, False, False
        r_c = 0
        c_c = 0
        while head:
            if r:
                ans[r_c][c_c] = head.val
                if c_c==c_e:
                    d = True
                    r = not r
                    r_c += 1
                    c_e -= 1
                else: c_c+=1
            elif d:
                ans[r_c][c_c] = head.val
                if r_c==r_e:
                    l = True
                    d = not d
                    c_c-=1
                    r_e -= 1
                else: r_c+=1
            elif l:
                ans[r_c][c_c] = head.val
                if c_c==c_s:
                    u = True
                    l = not l
                    r_c -= 1
                    c_s += 1
                else: c_c -= 1
            elif u:
                ans[r_c][c_c] = head.val
                if r_c==r_s:
                    r = True
                    u = not u
                    c_c += 1
                    r_s += 1
                else: r_c -=1
                
            head = head.next
        
        return ans



            

        