class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.token = dict()
        self.time = timeToLive    # store timeToLive and create dictionary

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.token[tokenId] = currentTime # store tokenId with currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime-self.time        # calculate limit time to filter unexpired tokens
        if tokenId in self.token and self.token[tokenId]>limit:    # filter tokens and renew its time
            self.token[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime-self.time       # calculate limit time to filter unexpired tokens
        c = 0
        for i in self.token:
            if self.token[i]>limit:         # count unexpired tokens
                c+=1
        return c


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)