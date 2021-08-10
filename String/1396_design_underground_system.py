class UndergroundSystem:

    def __init__(self):
        self.check_in = dict()
        self.records = dict()
        pass

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)
        pass

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.check_in and stationName != self.check_in[id][0]:
            station_pair = (self.check_in[id][0], stationName)
            travel_time = t - self.check_in[id][1]
            if station_pair in self.records:
                self.records[station_pair] = [self.records[station_pair][0] + travel_time, self.records[station_pair][1] + 1]
            else:
                self.records[station_pair] = [travel_time, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        station_pair = (startStation, endStation)
        if station_pair in self.records:
            return self.records[station_pair][0] / self.records[station_pair][1]
        return 0


def test_underground_system():
    us = UndergroundSystem()
    us.checkIn(45, "Leyton", 3)
    us.checkIn(32, "Paradise", 8)
    us.checkIn(27, "Leyton", 10)

    us.checkOut(45, "Waterloo", 15)
    us.checkOut(27, "Waterloo", 20)
    us.checkOut(32, "Cambridge", 22)

    assert abs(us.getAverageTime("Paradise", "Cambridge") - 14) < 1e-3, "wrong result"
    assert abs(us.getAverageTime("Leyton", "Waterloo") - 11) < 1e-3, "wrong result"

    us.checkIn(10, "Leyton", 24)
    assert abs(us.getAverageTime("Leyton", "Waterloo") - 11) < 1e-3, "wrong result"
    us.checkOut(10, "Waterloo", 38)
    assert abs(us.getAverageTime("Leyton", "Waterloo") - 12) < 1e-3, "wrong result"


if __name__ == '__main__':
    test_underground_system()
