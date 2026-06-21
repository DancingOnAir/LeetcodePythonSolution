from itertools import accumulate


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        return max([0] + list(accumulate(gain, initial=0)))


def test_largest_altitude():
    solution = Solution()
    assert solution.largestAltitude([-5,1,5,0,-7]) == 1
    assert solution.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0


if __name__ == "__main__":
    test_largest_altitude()
