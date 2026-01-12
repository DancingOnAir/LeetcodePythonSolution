from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] += 1
            diff[r + 1] -= 1

        coverage = 0
        for i in range(n):
            coverage += diff[i]
            if coverage < nums[i]:
                return False
        return True


def test_is_zero_array():
    solution = Solution()
    assert solution.isZeroArray([1, 0, 1], [[0, 2]]), 'wrong result'
    assert not solution.isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]), 'wrong result'


if __name__ == '__main__':
    test_is_zero_array()
