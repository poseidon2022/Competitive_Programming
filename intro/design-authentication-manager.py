class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token = defaultdict(int)
        self.timeToLive = timeToLive
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if self.token[tokenId] - currentTime > 0: self.token[tokenId] = currentTime + self.timeToLive
        else: del self.token[tokenId]
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for i in self.token:
            if self.token[i]-currentTime > 0: count+=1
        
        return count


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)