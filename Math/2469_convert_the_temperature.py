from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]


def test_convert_temperature():
    solution = Solution()
    assert solution.convertTemperature(36.50) == [309.65000, 97.70000], 'wrong result'
    assert solution.convertTemperature(122.11) == [395.26000, 251.79800], 'wrong result'


if __name__ == '__main__':
    test_convert_temperature()
