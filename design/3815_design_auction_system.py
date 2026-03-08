from collections import defaultdict
from heapq import heappop, heappush


class AuctionSystem:
    def __init__(self):
        # (userId, itemId) -> bidAmount
        self.amount = defaultdict(int)
        # item -> (bidAmount, userId)
        self.item = defaultdict(list)

    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
        self.amount[(userId, itemId)] = bidAmount
        heappush(self.item[itemId], (-bidAmount, -userId))

    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
        self.addBid(userId, itemId, newAmount)

    def removeBid(self, userId: int, itemId: int) -> None:
        self.amount.pop((userId, itemId), None)

    def getHighestBidder(self, itemId: int) -> int:
        high = self.item[itemId]
        while high:
            bidAmount, userId = -high[0][0], -high[0][1]
            if bidAmount == self.amount[(userId, itemId)]:
                return userId
            heappop(self.item[itemId])
        return -1


def test_auction_system():
    auctionSystem = AuctionSystem()
    auctionSystem.addBid(1,7,5)
    auctionSystem.addBid(2,7,6)
    assert auctionSystem.getHighestBidder(7) == 2, 'wrong result'
    auctionSystem.updateBid(1,7,8)
    assert auctionSystem.getHighestBidder(7) == 1, 'wrong result'
    auctionSystem.removeBid(2, 7)
    assert auctionSystem.getHighestBidder(7) == 1, 'wrong result'
    assert auctionSystem.getHighestBidder(3) == -1, 'wrong result'


if __name__ == '__main__':
    test_auction_system()
