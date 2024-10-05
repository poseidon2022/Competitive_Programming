# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        freq = 0
        ans = 0
        for char in allowed:
            freq |= 1 << (ord(char) - ord('a'))
        
        for word in words:
            char_count = 0
            for char in word:
                if not freq & (1 << (ord(char) - ord('a'))): break
                char_count += 1
            
            if char_count == len(word): ans += 1

        return ans
                
        