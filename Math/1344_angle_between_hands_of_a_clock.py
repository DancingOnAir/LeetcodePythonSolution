class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        dh = minutes / 2 + hour * 30
        dm = minutes * 6
        res = abs(dh - dm)
        return res if res <= 180 else 360 - res


def test_angle_clock():
    solution = Solution()
    assert solution.angleClock(12, 30) == 165, 'wrong result'
    assert solution.angleClock(3, 30) == 75, 'wrong result'
    assert solution.angleClock(3, 15) == 7.5, 'wrong result'


if __name__ == '__main__':
    test_angle_clock()
