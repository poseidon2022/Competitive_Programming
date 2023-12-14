class FrequencyTracker:

    def __init__(self):
        self.mine = defaultdict(int)        
        self.freq = defaultdict(int)
    def add(self, number: int) -> None:
        print(self.freq, number)
        if self.freq[self.mine[number]]:
            self.freq[self.mine[number]]-=1
            if not self.freq[self.mine[number]]: del self.freq[self.mine[number]]
        self.mine[number]+=1
        self.freq[self.mine[number]]+=1
    def deleteOne(self, number: int) -> None:
        if self.mine[number]:
            self.freq[self.mine[number]]-=1
            if not self.freq[self.mine[number]]: del self.freq[self.mine[number]]
            self.mine[number]-=1
            self.freq[self.mine[number]]+=1
        print(self.freq)
    def hasFrequency(self, frequency: int) -> bool:
        print(self.freq[frequency])
        return self.freq[frequency]


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)