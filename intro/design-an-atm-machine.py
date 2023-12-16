class ATM:

    def __init__(self):
        self._map = {0:20, 1:50, 2:100, 3:200, 4:500}
        self.mine = defaultdict(int)
    def deposit(self, banknotesCount: List[int]) -> None:
        for idx, val in enumerate(banknotesCount):
            self.mine[self._map[idx]]+=val
    def withdraw(self, amount: int) -> List[int]:
        dummy = self.mine.copy()
        print(self.mine)
        ans = deque([])
        flag = False
        for idx,val in enumerate([500,200,100,50,20]):
            if amount - val >= 0:
                wanted = amount//val
                if self.mine[val]>=wanted:
                    amount -= val*wanted
                    self.mine[val] -= wanted
                else:
                    amount -= val*self.mine[val]
                    self.mine[val] = 0
            
            ans.appendleft(dummy[val] - self.mine[val])
        
        if amount!=0:
            self.mine = dummy
            return [-1]
        return ans

        

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)