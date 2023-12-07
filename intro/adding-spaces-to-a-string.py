class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        ans = ''
        spaces = spaces[::-1]
        for idx,val in enumerate(s):
            if spaces and idx==spaces[-1]:
                ans+=' ' + val
                spaces.pop()
                continue
            ans+=val
        
        return ans

        