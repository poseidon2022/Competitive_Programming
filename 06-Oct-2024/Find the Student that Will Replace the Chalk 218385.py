# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        rem = k - ((k // sum(chalk))*sum(chalk))
        for idx, num in enumerate(chalk):

            if rem < num: return idx  
            else: rem -= num      