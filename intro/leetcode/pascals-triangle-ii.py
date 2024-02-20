class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        def pascal(row):
            if row == 0:
                return [1]
            if row == 1:
                return [1, 1]

            d = pascal(row - 1)
            mine = []
            for i in range(row - 1):
                mine.append(d[i] + d[i+1])

            return [1] + mine + [1]

        return pascal(rowIndex)
            
        