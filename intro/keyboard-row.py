class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            if i[0].lower() in "qwertyuiop": target = 1
            elif i[0].lower() in "asdfghjkl": target = 2
            else: target = 3
            flag = True
            for j in i:
                if (j.lower() in "qwertyuiop" and target!=1) or (j.lower() in "asdfghjkl" and target!=2) or (j.lower() in "zxcvbnm" and target!=3):
                    flag = not flag
                    break

            if flag: ans.append(i)
        return ans

        