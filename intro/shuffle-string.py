class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans = ['a' for _ in s]
        for i in range(len(s)):
            ans[indices[i]] = s[i]
        return ''.join(ans) 