class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.counter_1 = set()
        self.counter_0 = set(_ for _ in range(self.size))

    def fix(self, idx: int) -> None:
        self.counter_1.add(idx)
        self.counter_0.discard(idx)
    def unfix(self, idx: int) -> None:
        self.counter_1.discard(idx)
        self.counter_0.add(idx)
    def flip(self) -> None:
        self.counter_1, self.counter_0 = self.counter_0, self.counter_1
    def all(self) -> bool:
        return len(self.counter_1)==self.size
    def one(self) -> bool:
        return len(self.counter_1) > 0

    def count(self) -> int:
        return len(self.counter_1)
    def toString(self) -> str:
        ans = [0 for _ in range(self.size)]
        for i in self.counter_1: ans[i] = 1
        final = ''
        for i in ans: final+=str(i)
        return final
        
    

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()