class Solution:
    def trafficSignal(self, timer: int) -> str:
        if 0 == timer:
            return "Green"
        elif 30 == timer:
            return "Orange"
        elif 30 < timer <= 90:
            return "Red"
        return "Invalid"


def test_traffic_signal():
    solution = Solution()
    assert solution.trafficSignal(60) == "Red", 'wrong result'
    assert solution.trafficSignal(5) == "Invalid", 'wrong result'


if __name__ == '__main__':
    test_traffic_signal()
