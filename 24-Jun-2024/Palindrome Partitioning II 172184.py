# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:

        def isPalindrome(s):
            return s == s[::-1]
        
        @cache
        def helper(sub):
            
            if isPalindrome(sub):
                return 0

            if not sub:
                return 0

            min_cut = len(sub) - 1
            for i in range(1, len(sub)):
                if isPalindrome(sub[:i]):
                    min_cut = min(min_cut, 1 + helper(sub[i:]))
            return min_cut

        return helper(s)
