class Robot:

    def __init__(self, width: int, height: int):
        self.height, self.width = height, width
        self.prev = 0
        self.dir = 'East'
        self.cur = [0,0]
        self.perim = 2 * (self.height - 1)  + 2*(self.width - 1)
        self.east = self.width - 1
        self.north = self.width + self.height - 2
        self.west = (self.height - 1) + (2 * (self.width - 1))
        self.south = self.perim
    def step(self, num: int) -> None:
        final = (num + self.prev)%(self.perim)
        if final==0:
            self.dir = 'South'
            self.cur = [0,0]
        elif final<=self.east:
            self.dir = 'East'
            self.cur = [final ,0]
        elif final<=self.north:
            self.dir = 'North'
            self.cur = [self.width-1,final - (self.width - 1)]
        elif final<=self.west:
            self.dir = 'West'
            self.cur = [self.width - (final - (self. height + self.width - 2)) - 1 ,self.height-1]
        elif final<=self.south:
            self.dir = 'South'
            self.cur = [0,self.perim - final]
        self.prev = final
        #nums%(2r + 2c - 1)
        #east and west are always on a fixed row
        #north and south are always on a fixed column
        #calculate the offset from the range
        #U'RE GOOD TO GO!
    def getPos(self) -> List[int]:
        return self.cur
    def getDir(self) -> str:
        return self.dir
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()