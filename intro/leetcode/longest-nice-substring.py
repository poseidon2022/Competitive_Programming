class Solution:
    def longestNiceSubstring(self, s: str) -> str:

        self.ans = ''
        mine = defaultdict(int)
        def helper(string):
            
            if mine[string]:
                return
            if not string:
                return

            mine[string] += 1
            f = False
            for i in range(len(string)):
                if string.count(string[i].swapcase())==0:
                    f = not f
                    break
            
            if not f: 
                if len(string) > len(self.ans): 
                    self.ans = string
                return
            
            helper(string[:len(string)-1])
            helper(string[1:len(string)])
            
        
        helper(s)
        return self.ans