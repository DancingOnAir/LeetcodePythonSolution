from math import acos, degrees


class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        def cal_angle(a: int, b: int, c: int) -> float:
            return degrees(acos((b * b + c * c - a * a) / (2 * b * c)))

        a, b, c = sorted(sides)
        if a + b <= c:
            return []
        res = [cal_angle(a, b, c), cal_angle(b, a, c), cal_angle(c, a, b)]
        return res


def test_internal_angles():
    solution = Solution()
    assert solution.internalAngles([3, 4, 5]) == [36.86990, 53.13010, 90.00000], 'wrong result'
    assert solution.internalAngles([2, 4, 2]) == [], 'wrong result'


if __name__ == '__main__':
    test_internal_angles()
