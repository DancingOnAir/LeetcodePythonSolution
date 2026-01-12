class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.tokens = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokens and currentTime < self.tokens[tokenId]:
            self.tokens[tokenId] = currentTime + self.time_to_live

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(v > currentTime for v in self.tokens.values())


def test_authentication_manager():
    authenticationManager = AuthenticationManager(5)
    authenticationManager.renew("aaa", 1)
    authenticationManager.generate("aaa", 2)
    assert authenticationManager.countUnexpiredTokens(6) == 1, 'wrong result'
    authenticationManager.generate("bbb", 7)
    authenticationManager.renew("aaa", 8)
    authenticationManager.renew("bbb", 10)
    assert authenticationManager.countUnexpiredTokens(15) == 0, 'wrong result'


if __name__ == '__main__':
    test_authentication_manager()
