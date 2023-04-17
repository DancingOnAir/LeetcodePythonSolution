from typing import List
from collections import Counter


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        return len(nums) - max(Counter(nums).values())

    def maximizeGreatness2(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums:
            if nums[i] < x:
                i += 1
        return i

    def maximizeGreatness1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        res, left, right = 0, n - 2, n - 1
        nums.sort()
        while left >= 0:
            if nums[left] < nums[right]:
                right -= 1
                res += 1
            left -= 1
        return res


def test_maximize_greatness():
    solution = Solution()
    assert solution.maximizeGreatness([1, 3, 5, 2, 1, 3, 1]) == 4, 'wrong result'
    assert solution.maximizeGreatness([1, 2, 3, 4]) == 3, 'wrong result'


if __name__ == '__main__':
    test_maximize_greatness()
