class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.values = defaultdict(str)
        self.start = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:

        ans = []
        self.values[idKey] = value
        if idKey==self.start:
            while self.values[idKey]:
                ans.append(self.values[idKey])
                idKey+=1
                self.start+=1
        return ans



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)