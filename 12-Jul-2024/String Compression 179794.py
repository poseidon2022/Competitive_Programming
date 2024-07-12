# Problem: String Compression - https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        i,j = 0,0
        kept,count = 0,0
        while j<len(chars):
            if chars[i]==chars[j]: count+=1
            else:
                chars[kept] = chars[j-1]
                kept+=1
                if count>1:
                    count = str(count)
                    for _ in count:
                        chars[kept] = _
                        kept+=1
                i = j
                count = 1
            j+=1
        
        chars[kept] = chars[j-1]
        kept+=1
        if count>1:
            count = str(count)
            for _ in count:
                chars[kept] = _
                kept+=1
        return len(chars[:kept])


        