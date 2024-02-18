class RecentCounter:

    def __init__(self):
        self.pin = []
    def ping(self, t: int) -> int:
        self.pin.append(t)
        count = 0
        for i in range(len(self.pin) - 1, -1, -1):
            if t - 3000<=self.pin[i] and self.pin[i]<=t: count+=1
            else: break
        
        return count



        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)