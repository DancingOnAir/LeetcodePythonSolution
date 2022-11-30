from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return len(set(nums[i] + nums[n - i - 1] for i in range(n // 2)))


def test_distinct_averages():
    solution = Solution()
    assert solution.distinctAverages([4, 1, 4, 0, 3, 5]) == 2, 'wrong result'
    assert solution.distinctAverages([1, 100]) == 1, 'wrong result'


if __name__ == '__main__':
    test_distinct_averages()
