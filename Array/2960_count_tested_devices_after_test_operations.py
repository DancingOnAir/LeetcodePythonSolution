from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        for x in batteryPercentages:
            res += x > res
        return res


def test_count_tested_devices():
    solution = Solution()
    assert solution.countTestedDevices([1,1,2,1,3]) == 3, 'wrong result'
    assert solution.countTestedDevices([0,1,2]) == 2, 'wrong result'
    assert solution.countTestedDevices([0,1,2]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_tested_devices()
