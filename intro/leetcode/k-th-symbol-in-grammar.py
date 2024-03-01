class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(k, n):
            if k == 1:
                return 0
            n = math.ceil(math.log(k, 2)) + 1
            return not helper(k - 2 ** (n - 2), n - 1)
        
        return int(helper(k, n))
        