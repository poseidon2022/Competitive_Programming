# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.start = defaultdict(list)
        self.place = defaultdict(list)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start[id].append(stationName)
        self.start[id].append(t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.place[(self.start[id][0], stationName)].append(t - self.start[id][1])
        del self.start[id]
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = 0
        n = len(self.place[(startStation, endStation)])
        for i in self.place[(startStation, endStation)]:
            total+=i
        return total/n




# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)