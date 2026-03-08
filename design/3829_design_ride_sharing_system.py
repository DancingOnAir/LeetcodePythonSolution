from typing import List
from heapq import heappop, heappush
from collections import deque


class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.waiting_riders = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        while self.riders and self.riders[0] not in self.waiting_riders:
            self.riders.popleft()
        if not self.riders or not self.drivers:
            return [-1, -1]
        return [self.drivers.popleft(), self.riders.popleft()]

    def cancelRider(self, riderId: int) -> None:
        self.waiting_riders.discard(riderId)


def test_ride_sharing_system():
    obj = RideSharingSystem()
    obj.addRider(3)
    obj.addDriver(2)
    obj.addRider(1)
    assert obj.matchDriverWithRider() == [2, 3]
    obj.addDriver(5)
    obj.cancelRider(3)
    assert obj.matchDriverWithRider() == [5, 1]
    assert obj.matchDriverWithRider() == [-1, -1]


if __name__ == '__main__':
    test_ride_sharing_system()
